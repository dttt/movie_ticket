# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset

from helper.misc import Message
from users.forms import SignUpForm, LoginForm
from users.models import CustomUser


@transaction.atomic
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

    #if request.user.is_authenticated:
    #    return redirect(reverse('home'))

    return render(request, 'signup.html', {"form": form})


def signin(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                # Redirect when using login_required()
                if (request.GET.get('next', False)):
                    return redirect(request.GET['next'])

                return redirect(reverse('home'))
        else:
            errors = {Message.EMAIL_PASSWORD_NOT_MATCH}
            return render(
                request,
                'login.html',
                {"form": form, "errors": errors}
            )

    #if request.user.is_authenticated:
    #    return redirect(reverse('home'))

    return render(request, 'login.html', {"form": form})


def signout(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if user == request.user:
        return render(request, 'user-profile.html', {'user': user})


def reset_password(request):
    return password_reset(request, 'password-reset.html')
