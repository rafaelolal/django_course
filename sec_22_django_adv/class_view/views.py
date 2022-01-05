from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from class_view.models import School

class IndexView(TemplateView):
    template_name = 'index.html'

# Create your views here.
class SchoolListView(ListView):
    model = School
    # so common to return a context dict here that it is done automatically
    # done automatically
    # returns in the context:
    # school_list
    # to change default:
    # context_object_name = "schools"

class SchoolDetailView(DetailView):
    # returns model name in lowercase
    # better to change it yourself:
    context_object_name = "school_detail"
    model = School
    template_name = 'class_view/school_detail.html'