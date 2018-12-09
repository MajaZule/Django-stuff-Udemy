from django.conf.urls import url
from First_App import views

urlpatterns = [
    url('', views.index, name='index'),
]
