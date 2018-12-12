from django.conf.urls import url
from basic_app import views

urlpatterns = [
    url('', views.form_name_view, name = 'forms')
]
