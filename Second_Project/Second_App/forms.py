from django.forms import ModelForm
from django.core import validators
from Second_App.models import MyModel


class MyFormModel(ModelForm):

    class Meta:
        model = MyModel
        fields = [ "first_name", "last_name", "email"]
