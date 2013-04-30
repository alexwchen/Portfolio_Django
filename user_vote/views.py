from django.http import HttpResponse, HttpResponseRedirect
from rankProj.models import Project, Feature, Project_Type
from user_vote.models import User_ID, User_Event, User_Project_Lock
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.conf import settings
import datetime

########################################################
###   Increment User Vote For Each Project
###   User May Vote Once Per Day
###   Called When Thumb icon being clicked on portfolio page
###
###   Future:        
###     1. Change the Lock From Remote Addr to Sessions
###     2. Calculate User Votes Associate With Time
###
###
########################################################
def voting_project(request):
    
    # all message variable = Debugging Message
    message = 'voting_project_start'
    
    # next 3 if conditions is how you handle jquery request on Django
    if request.is_ajax():
        client_address = request.session.session_key
	request.session.set_expiry(1209600)
        request.session["fav_color"] = "blue"
	if request.method == u'GET':
            GET = request.GET
            if GET.has_key(u'current_page_url'): # this is the name of the project voted
                input_link = str(GET[u'current_page_url'])
                try:
                    # get corressponding user info and check lock info
                    MyUser = User_ID.objects.get(user_ip = client_address)
                    proj_lock = User_Project_Lock.objects.filter(user_id = MyUser).get(project_link = input_link)
                    
                    # calculate when is the last time this user votes
                    entry_old = proj_lock.project_lock 
                    entry_new = datetime.datetime.now()
                    year_diff = entry_old.year - entry_new.year
                    month_diff = entry_old.month - entry_new.month
                    day_diff = entry_old.day - entry_new.day
                    hour_diff = entry_old.hour - entry_new.hour
                    minute_diff = entry_old.minute - entry_new.minute
                    second_diff = entry_old.second - entry_new.second

                    # voting time is set for 24 hours, user are not allowed to vote twice within a day
                    if (int(year_diff)!=0 or int(month_diff)!=0 or int(day_diff)!=0):
                        # increment votes
                        vote = Project.objects.get(link = input_link) 
                        vote.vote_up = vote.vote_up + 1
                        vote.save()
                        proj_lock.project_lock = datetime.datetime.now()
                        proj_lock.save()
                        message = "just voted"
                    else:
                        # lock from voting, nothing happens
                        message = "vote too much" + '\n' + str(repr(entry_new)) + '\n'  + str(repr(entry_old))
                except:
                    message = "Error on voting projects"
    return HttpResponse(message)

#############################################################
###   Record Current Time When User Visits A Page
###   Function 'window_unload_time_stemp' Will Record Time When User Left
###             A Page 
###
############################################################

def window_load_time_stemp(request):
    
    # first 3 if conditions is how you handle jquery request
    if request.is_ajax():
        client_address = request.session.session_key
	request.session.set_expiry(1209600)
        request.session["fav_color"] = "blue"
        if request.method == u'GET':
            GET = request.GET
            if GET.has_key(u'current_page_url'):
                p_link = GET[u'current_page_url'] # get what page user visits
                
                # for returning users, we check if ip is in database
                # first time visitors go to except
                try:
                    # Message Variable = Debugging Use
                    message = 'Success: Returning User'

                    # get user info and current time
                    Old_User = User_ID.objects.get(user_ip = client_address)
                    entry_new = datetime.datetime.now()

                    UserEventCreate = User_Event(
                                                user_id = Old_User, #record ip
                                                enter_time = entry_new, #record current time
                                                page_link = p_link, # record what page
                                                )
                    UserEventCreate.save()
                except:
                    # First time this ip visit my site
                    # create new user info table, start tracking time on page
                    UserCreate = User_ID(user_ip = client_address)
                    UserCreate.save()
                    UserEventCreate = User_Event(
                                                user_id = UserCreate,
                                                enter_time = datetime.datetime.now(),
                                                page_link = p_link,
                                                )
                    UserEventCreate.save()

                    # set up a new lock for user
                    # lock date is set to very old, but it won't affect the correctness of the algorithm
                    for proj in Project.objects.all():
                        User_Create_Project_Lock = User_Project_Lock(
                            user_id = UserCreate,
                            project_lock = datetime.datetime(2011,12,12,0,0),
                            project_link = proj.link,
                        )
                        User_Create_Project_Lock.save()
                    message = 'Success: First Time Visiting'
    else:
        message = 'Error: some other request that is not Ajax?'
    return HttpResponse(message)

#############################################################
###   Record Current Time When User Left A Page & Calculate
###   Total Time Spent on This Page
###
###   Function 'window_load_time_stemp' Will Record Time When User Enter
###             A Page 
###
############################################################

def window_unload_time_stemp(request):
    
    # first 3 if conditions is how you handle jquery request
    if request.is_ajax():
        client_address = request.session.session_key
        request.session["fav_color"] = "blue"
        if request.method == u'GET':
            GET = request.GET
            if GET.has_key(u'current_page_url'):
                p_link = GET[u'current_page_url'] # get what page user visits
                
                # for returning users, we check if ip is in database
                # first time visitors go to except
                try: 
                    # Message Variable = Debugging Use
                    message = 'window unload processing'
                    
                    # calcuate time spent for last page
                    UserIDRetrieve = User_ID.objects.filter(user_ip=client_address)
                    UserEventRetrieve = User_Event.objects.filter(user_id=UserIDRetrieve).order_by('-enter_time')[0]
                    
                    entry_old = UserEventRetrieve.enter_time
                    entry_new = datetime.datetime.now()

                    year_diff = entry_old.year - entry_new.year
                    month_diff = entry_old.month - entry_new.month
                    day_diff = entry_old.day - entry_new.day
                    hour_diff = entry_old.hour - entry_new.hour
                    minute_diff = entry_old.minute - entry_new.minute
                    second_diff = entry_old.second - entry_new.second
                    # checking if request is the same day
                    # we will also know what page did user leave the site by doing this
                    # WINDOWS LOAD CAN REPLACE THE NEED OF THIS FUNCTION
                    total_secs = -1
                    if (int(year_diff)==0 and int(month_diff)==0 and int(day_diff)==0 ):
                        # Calculate difference in seconds
                        total_secs = int(hour_diff)*3600 + int(minute_diff)*60 + int(second_diff)
                    message = str(-total_secs)
                    
                    # create a new time record for the last page
                    UserEventRetrieve.time_on_page = (-total_secs)
                    UserEventRetrieve.save()
                except:
                    message = 'windows unload fails, why?'
    else:
        message = 'Error: some other request that is not Ajax?'
    return HttpResponse(message)


####################################################################
###   Ranking Filter
###   Can Be Ranked By Project Type, Complete Time, Ranking Algorithm 
###   Handle Jquery Request, Return List Of Project ID
###   Future:
###    *1. If server don't support python upto 2.7, importing "simpleJson" is a problem.
###     2. Recommend For You is still under construction
###     3. Best Rank didn't involve user time on page
####################################################################

from django.utils import simplejson
def rankfilter(request):

    # message variable = debuggin use
    message = "welcome to rankfilter, you should not see this" 
    
    # next 3 if conditions handle jquery request
    if request.is_ajax():
        if request.method == u'GET':
            GET = request.GET
            if GET.has_key(u'filter_option'):
                filter_option = GET[u'filter_option']
                
                # Dictionary is created to return sorted list to client
                j_dict = {'total':0, 'sortedlist':[]} 
                
                # Get total # of projects
                allobj = len(Project.objects.all())
                j_dict['total'] = allobj
                
                # Machine Learning 
                if filter_option =='Machine Learning':
                    # Get all type in ML, return sortedlist
                    mlproj = Project_Type.objects.filter(project_type="ML")
                    mllist = []
                    for proj in mlproj:
                        tmp = proj.project
                        mllist.append(tmp.id)
                    j_dict['sortedlist'] = mllist
                    json_return = simplejson.dumps(j_dict)
                    return HttpResponse(json_return)
                
                # Get all type in HCI, return sortedlist
                if filter_option =='Human Computer Interface':
                    hciproj = Project_Type.objects.filter(project_type="HCI")
                    hcilist = []
                    for proj in hciproj:
                        tmp = proj.project
                        hcilist.append(tmp.id)
                    j_dict['sortedlist'] = hcilist
                    json_return = simplejson.dumps(j_dict)
                    return HttpResponse(json_return)
                
                # Web: Not Activated Yet
                if filter_option =='Web':
                    webproj = Project_Type.objects.filter(project_type="WEB")
                    weblist = []
                    for proj in webproj:
                        tmp = proj.project
                        weblist.append(tmp.id)
                    j_dict['sortedlist'] = weblist
                    json_return = simplejson.dumps(j_dict)
                    return HttpResponse(json_return)
                
                # Publications
                if filter_option =='Publications':
                    webproj = Project_Type.objects.filter(project_type="PUB")
                    weblist = []
                    for proj in webproj:
                        tmp = proj.project
                        weblist.append(tmp.id)
                    j_dict['sortedlist'] = weblist
                    json_return = simplejson.dumps(j_dict)
                    return HttpResponse(json_return)

                # All Projects 
                if filter_option =='All Projects':
                    allproj = Project_Type.objects.filter(project_type="ALL")
                    alllist = []
                    for proj in allproj:
                        tmp = proj.project
                        alllist.append(tmp.id)
                    j_dict['sortedlist'] = alllist
                    json_return = simplejson.dumps(j_dict)

                    return HttpResponse(json_return)
                
                # Best: Havn't add user time on page
                if filter_option =='Best':
                    
                    bestproj = Project.objects.order_by('-base_vote')
                    bestlist = []
                    for proj in bestproj:
                        bestlist.append(proj.id)
                    j_dict['sortedlist'] = bestlist
                    json_return = simplejson.dumps(j_dict)
                    
                    return HttpResponse(json_return)

                # Most Recent
                if filter_option =='Most Recent':
                    timeproj = Project.objects.order_by('-complete_date')
                    timelist = []
                    for proj in timeproj:
                        timelist.append(proj.id)
                    j_dict['sortedlist'] = timelist
                    json_return = simplejson.dumps(j_dict)
                    return HttpResponse(json_return)
                
                # Less Recent 
                if filter_option =='Less Recent':
                    timeproj = Project.objects.order_by('complete_date')
                    timelist = []
                    for proj in timeproj:
                        timelist.append(proj.id)
                    j_dict['sortedlist'] = timelist
                    json_return = simplejson.dumps(j_dict)

                    return HttpResponse(json_return)

    return HttpResponse(message)

