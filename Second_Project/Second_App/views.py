from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<em>My Second Project</em>')

def help(request):
    dict = {'help_me':'Help Page'}
    return render(request, 'second_app/help_page.html', context=dict)
# Create your views here.
