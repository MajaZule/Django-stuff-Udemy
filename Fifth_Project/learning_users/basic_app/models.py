from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model): # model class to add in additional info that the defaut user does not have
# do not inherit directly - it screws up stuff

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'basic_app/profile_pics', blank = True) #profile_pics needs to be subdirectory in MEDIA_DIR

    def __str__(self):
        return self.user.username
