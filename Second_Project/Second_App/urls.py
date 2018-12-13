from django.conf.urls import url
from Second_App import views

urlpatterns = [
    url('', views.form_name_view, name = 'model_form')
]
