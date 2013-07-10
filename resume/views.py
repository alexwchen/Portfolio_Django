from django.http import HttpResponse
from resume.models import Education, Job, Affiliation, Contact, Images
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
