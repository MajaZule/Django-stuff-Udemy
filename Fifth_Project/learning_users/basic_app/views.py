from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm


def index(request):
    return render(request, 'basic_app/index.html')

def register(request):

    registered = False
    # we assume they are not registered

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # we are grabbing user form, setting it to the user, hashing the password and saving it to database

            profile = profile_form.save(commit = False)
            profile.user = user
            # sets up onetoone relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

# WORKFLOW: 1. registration view
#           2. check if user is registered(assume it is not with registered = False)
#           3. if request = post, we grab info from the forms
#           4. check if both forms are valid
#           5. if they are, we grab everything from the base user form
#           6. grab the profile form and double check it to see if it has a picture iin it before we save it
#           7. set register = True
#           8. if tere is an error, print it out
#           9. if request != post, we set forms(user_form and profile_form)
#           10. return render
