from django.shortcuts import render
from django.http import HttpResponse
from First_App.models import Topic, Webpage, AccessRocord
# Create your views here.

def index(request):
    webpages_list = AccessRocord.objects.order_by('date') #order_by is a sql command
    date_dict = {'access_records': webpages_list}
    return render(request, 'First_App/index.html', context = date_dict)
