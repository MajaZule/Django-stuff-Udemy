from django import forms
from django.core import validators


#custom validation function
#def check_for_z(value):
#    if value[0].lower != 'z':
#        raise forms.ValidationError("Name needs to start with z")


class Form_name(forms.Form):
    name = forms.CharField() # also here pass into brackets validators = [check_for_z]
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again: ')
    text = forms.CharField(widget = forms.Textarea)
#    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxValueValidator(0)])

#grabbing all clean data at once
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Please make sure emails match")


#we can replace this code with validators call
    #def clean_botcatcher(self):
        #botcatcher = self.cleaned_data['botcatcher']
        #if len(botcatcher) > 0: #because bot would add in a value
            #raise forms.ValidationError("It's a bot!")
        #return botcatcher
