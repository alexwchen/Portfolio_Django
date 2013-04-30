from django.http import HttpResponse
from education.models import Material, Material_Type
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
import datetime
from django.conf import settings

def education_rank(request):
    return HttpResponse('hello')
