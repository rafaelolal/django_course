from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    my_dict = {'insert_me': "Hello, I am from second_app/views.py"}
    return render(request, 'second_app/help.html', context=my_dict)