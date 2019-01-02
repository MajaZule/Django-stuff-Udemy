from django.urls import path
from django.contrib.auth import views as auth_views
# with this we don't have to create login and logout view
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # for login we have to connect it to the template, for logout it has a default view
    # logout goes to homepage once we log out
    path('signup/', views.SignUp.as_view(), name='signup'),
]
