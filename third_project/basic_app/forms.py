from django import forms
from django.core import validators


#custom validation function
def check_for_z(value):
    if value[0].lower != 'z':
        raise forms.ValidationError("Name needs to start with z")


class Form_name(forms.Form):
    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxValueValidator(0)])


#we can replace this code with validators call
    #def clean_botcatcher(self):
        #botcatcher = self.cleaned_data['botcatcher']
        #if len(botcatcher) > 0: #because bot would add in a value
            #raise forms.ValidationError("It's a bot!")
        #return botcatcher
