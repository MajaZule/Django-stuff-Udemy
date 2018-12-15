from django.shortcuts import render


def index(request):
    context_dict = {'text':'hello world', 'number':300}
    return render(request, 'basic_app/index.html', context_dict)

def base(request):
    return render(request, 'basic_app/base.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')
