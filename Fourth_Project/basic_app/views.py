from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html')

def base(request):
    return render(request, 'basic_app/base.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
