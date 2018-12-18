from django.conf.urls import url
from basic_app import views
from django.urls import path


app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name = 'list'), #name is for url template tagging
    path('<int:pk>/', views.SchoolDetailView.as_view(), name = 'detail')
]
