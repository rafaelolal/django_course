from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import Topic, WebPage, AccessRecord

# Create your views here.
def index(request):
    pages = AccessRecord.objects.order_by('date')
    date = {'records': pages}

    return render(request, 'first_app/index.html', context=date)