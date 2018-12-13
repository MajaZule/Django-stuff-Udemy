from django.db import models


#class User(models.Model):
#    first_name = models.CharField(max_length = 200, unique = True)
#    last_name = models.CharField(max_length = 200, unique = True)
#    email = models.EmailField(max_length = 200, unique = True)

class MyModel(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200, unique = True)

# Create your models here.
