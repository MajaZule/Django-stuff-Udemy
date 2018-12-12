from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'basic_app/index.html')

def form_name_view(request):
    form = forms.Form_name()

    if request.method == 'POST':
        form = forms.Form_name(request.POST)

        if form.is_valid():
            #do sth code
            print("Validation comlete")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'basic_app/form_page.html', {'form' : form})
# Create your views here.
