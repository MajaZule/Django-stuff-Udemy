from django.shortcuts import render
from django.http import HttpResponse
from Second_App.models import User

def index(request):
    return render(request, 'Second_App/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'Second_App/users.html', context = user_dict)
