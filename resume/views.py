from django.http import HttpResponse
from resume.models import Education, Job, Affiliation, Contact, Images
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.conf import settings

def resume_display(request):
    Edu =  Education.objects.all()
    Aff =  Affiliation.objects.all()
    TechJobs =  sorted(Job.objects.filter(job_type = 'tech'), reverse=True)
    CommJobs =  sorted(Job.objects.filter(job_type = 'comm'), reverse=True)
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
    FullPath = request.get_full_path()    
    Imagelist = Images.objects.all()
    return render_to_response(
        'resume/contact.html',
        {
           'Contact': Contacts,
           'Images':Imagelist,
           'FullPath': FullPath,
        }
    )
