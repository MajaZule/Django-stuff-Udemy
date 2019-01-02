from django.db import models
from django.contrib import auth
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return '@{}'.format(self.username)
        # username is an attribute that comes built in with User
