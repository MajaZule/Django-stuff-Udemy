from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy


#class CBView(View):
#    def get(self, request):
#        return HttpResponse('Class based views are cool')


class IndexView(TemplateView):
    template_name = 'index.html'
    #'index.html' under template folder
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['injectme'] = 'BASIC INJECTION'
#        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    # define your own context object name that is going to return the list of all schools inside
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
