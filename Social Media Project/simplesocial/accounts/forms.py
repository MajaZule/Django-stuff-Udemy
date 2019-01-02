from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        # when user comes in and is ready to sign up,
        # we call user authorisation form from auth.forms
        # and we set up the meta class with fields user can access when signing up (fields)
        # if we want labels on form:
        # under init we set up label for field from formy.py view (Display Name)
        # self.fields we don't need to do, this is for our own customisation
