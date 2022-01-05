from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
    DetailView, CreateView,
    UpdateView, DeleteView)

from django.urls import reverse_lazy

from class_view.models import School

class IndexView(TemplateView):
    template_name = 'index.html'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.request.user
    #     context["ticket_list"] = user.ticket_set.all()
    #     return context

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

class SchoolCreateView(CreateView):
    fields = ['name', 'principal', 'location']
    model = School

class SchoolUpdateView(UpdateView):
    fields = ['principal', 'name']
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("class_view:list")