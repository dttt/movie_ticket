from django.shortcuts import render, redirect

from users.forms import SignUpForm
from users.models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data(request.POST)
            user = CustomUser(
                email=user_input['email'],
                name=user_input['name'],
                card_id=user_input['card_id'],
                tel=user_input['tel'],
                date_of_birth=user_input['date_of_birth'],
            )

            # Check password and password confirmation is match?
            password = user_input['password']
            password_confirmation = user_input['password_confirmation']

            user.set_password(user_input['password'])
            user.save()
            return redirect()
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {"form": form})


def login(request):
    pass
