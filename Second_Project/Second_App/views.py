from django.shortcuts import render
#from django.http import HttpResponse
from . import forms
from Second_App.models import MyModel
#from Second_App.forms import MyFormModel


def index(request):
    return render(request, 'Second_App/index.html')

def form_name_view(request):
    form = forms.MyFormModel()

    if request.method == 'POST':
        form = forms.MyFormModel(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid Form')

    return render(request, 'Second_App/login_page.html', {'form' : form})
