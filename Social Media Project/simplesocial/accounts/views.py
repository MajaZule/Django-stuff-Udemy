from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView
from django.contrib.auth import login, logout


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    # once user signs up, we redirect them to login page
    template_name = 'accounts/signup.html'
