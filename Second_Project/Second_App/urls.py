from django.conf.urls import url
from Second_App import views

urlpatterns = [
    url('', views.help, name = 'help')
]
