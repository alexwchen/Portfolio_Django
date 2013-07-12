from django.http import HttpResponse
from resume.models import Education, Job, Affiliation, Contact, Supervisor, Supervisor_Affiliation, Supervisor_Department, Supervisor_Famous_paper
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.conf import settings

def resume_display(request):
    Edu =  Education.objects.all()
    Aff =  Affiliation.objects.all()
    TechJobs =  Job.objects.filter(job_type = 'tech').order_by('end_date').reverse()
    CommJobs =  Job.objects.filter(job_type = 'comm').order_by('end_date').reverse()
    FullPath = request.get_full_path()    
        
    return render_to_response(
        'resume/resume_display.html',
        {
           'Education': Edu,
           'Affiliation': Aff,
           'TechJobs': TechJobs,
           'CommJobs': CommJobs,
           'FullPath': FullPath,
        }
    )


def contact_display(request):
    Contacts =  Contact.objects.get(pk=1)
    Supervisors =  Supervisor.objects.all()
    #hi = Supervisor_Affiliation.objects.filter(supervisor=Supervisors[2])
    #print hi
    supervisor_list = []    
    for supervisor_for_loop in Supervisors:
        s = {}
        #print supervisor_for_loop
        affiliation = Supervisor_Affiliation.objects.filter(supervisor = supervisor_for_loop)
        department = Supervisor_Department.objects.filter(supervisor = supervisor_for_loop)
        famous_paper = Supervisor_Famous_paper.objects.filter(supervisor = supervisor_for_loop)

        s['affiliation'] = affiliation
        s['department'] = department
        s['famous_paper'] = famous_paper 
        s['supervisor'] = supervisor_for_loop 
        s['research_interest'] = str(supervisor_for_loop.research_interest).split(',')
        supervisor_list.append(s) 

        print s['affiliation'][0]
    FullPath = request.get_full_path()    
    #Imagelist = Images.objects.all()
    return render_to_response(
        'resume/contact.html',
        {
           'Contact': Contacts,
           #'Images':Imagelist,
           'FullPath': FullPath,
           'Supervisors': Supervisors,
           'Supervisor_detail': supervisor_list
        }
    )
