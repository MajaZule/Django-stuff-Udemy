from django.db import models

class Topic(models.Model): #this is inheritance
    top_name = models.CharField(max_length = 300, unique = True) #unique so u don't have duplicate names

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    name = models.CharField(max_length = 300, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name


class AccessRocord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
