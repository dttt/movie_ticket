from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from users.forms import SignUpForm, LoginForm
from users.models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #user_input = form.cleaned_data(request.POST)
            user = CustomUser(
                email=request.POST['email'],
                name=request.POST['name'],
                card_id=request.POST['card_id'],
                tel=request.POST['tel'],
                date_of_birth=request.POST['date_of_birth'],
            )

            user.set_password(request.POST['password'])
            user.save()
            return redirect(reverse('home'))
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {"form": form})


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {"form": form})
