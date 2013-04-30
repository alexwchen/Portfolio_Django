from django.http import HttpResponse
from rankProj.models import Project, Feature
from user_vote.models import User_ID, User_Project_Lock, User_Event
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
import datetime
from django.conf import settings

def show_rank(request):
    AllProj =  Project.objects.all()
    FullPath = request.get_full_path()    
    client_address = request.session.session_key
    request.session["fav_color"] = "blue"
    try:
        # Calculate Like Lock
        MyUser = User_ID.objects.get(user_ip = client_address)
        Like_Lock = {}
        for proj in AllProj:
            lock_time = User_Project_Lock.objects.filter(user_id = MyUser).get(project_link = proj.link)
        
            # Calcuate if locked
            entry_old = lock_time.project_lock 
            entry_new = datetime.datetime.now()
            year_diff = entry_old.year - entry_new.year
            month_diff = entry_old.month - entry_new.month
            day_diff = entry_old.day - entry_new.day
            if (int(year_diff)!=0 or int(month_diff)!=0 or int(day_diff)!=0):
                # Not Locked
                Like_Lock[proj.link] = 1
            else:
                # Locked
                Like_Lock[proj.link]=0
    except:
        # First time this ip visit my site
        # Create new user table
        # Intitialize voting lock
        # Start tracking time user spent on each page
        UserCreate = User_ID(user_ip = client_address)
        UserCreate.save()
        for proj in Project.objects.all():
            User_Create_Project_Lock = User_Project_Lock(
                user_id = UserCreate,
                project_lock = datetime.datetime(2011,12,12,0,0),
                project_link = proj.link,
            )
            User_Create_Project_Lock.save()
        
        Like_Lock = {}
        for proj in AllProj:    
            Like_Lock[proj.link] = 1
        
    return render_to_response(
        'rankProj/show_rank.html',
        {
           'AllProj': AllProj,
           'FullPath': FullPath,
           'Like_Lock': Like_Lock,
        }
    )

def show_proj(request, proj_title):
    
    P_object = Project.objects.get(link = proj_title)
    F_object = Feature.objects.filter(project = P_object.id).order_by('feature_order')
    FullPath = request.get_full_path()    

    return render_to_response(
        'rankProj/show_proj.html',
        {
            'project': P_object,
            'featurelist': F_object,
            'FullPath': FullPath,
        }
    )

def publication_rank(request):
    
    P_object = Project.objects.all()
    FullPath = request.get_full_path()    
    Publist = []
    for i in P_object:
        if i.PDF !='none':
            Publist.append(i)

    return render_to_response(
        'rankProj/publication_rank.html',
        {
            'publications': Publist,
            'FullPath': FullPath,
        }
    )


def publication_link(request, proj_title):
    
    P_object = Project.objects.get(link = proj_title)
    F_object = Feature.objects.filter(project = P_object.id).order_by('feature_order')
    FullPath = request.get_full_path()    

    return render_to_response(
        'rankProj/show_proj.html',
        {
            'project': P_object,
            'featurelist': F_object,
            'FullPath': FullPath,
        }
    )





