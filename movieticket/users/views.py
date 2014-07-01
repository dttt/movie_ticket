# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset
from django.contrib import messages

from helper.misc import Message
from users.forms import SignUpForm, LoginForm, EditForm, EditPasswordForm
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
            return redirect(reverse('user:signin'))
    else:
        form = SignUpForm()

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
                messages.add_message(
                    request, messages.SUCCESS, Message.welcome(user.name))
                # Redirect when using login_required()
                if (request.GET.get('next', False)):
                    return redirect(request.GET['next'])

                return redirect(reverse('home'))
        else:
            messages.add_message(
                request, messages.ERROR, Message.EMAIL_PASSWORD_NOT_MATCH)
            return render(
                request,
                'login.html',
                {"form": form}
            )
    return render(request, 'login.html', {"form": form})


def signout(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def profile(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if user == request.user:
        return render(request, 'user-profile.html', {'user': user})


@login_required
def edit(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if user == request.user:
        if request.method == 'POST':
            form = EditForm(request.POST)
            if form.is_valid():
                user.name = request.POST['name']
                user.card_id = request.POST['card_id']
                user.address = request.POST['address']
                user.tel = request.POST['tel']
                user.date_of_birth = request.POST['date_of_birth']
                user.save()
        # Initial data for form
        data = {
            'name': user.name,
            'address': user.address,
            'tel': user.tel,
            'card_id': user.card_id,
            'date_of_birth': user.date_of_birth
        }
        form = EditForm(initial=data)

        return render(
            request,
            'user-edit.html',
            {'form': form}
        )
    else:
        messages.add_message(
            request, messages.ERROR, Message.PERMISSION_DENIED)
        return redirect(reverse('users:signin'))


@login_required
def edit_password(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if user == request.user:
        if request.method == 'POST':
            form = EditPasswordForm(request.POST)
            if form.is_valid():
                old_password = request.POST['old_password']
                if user.check_password(old_password):
                    user.set_password(request.POST['password'])
                    user.save()
                    messages.add_message(
                        request, messages.SUCCESS, Message.EDITED_PASSWORD)
                else:
                    messages.add_message(
                        request, messages.ERROR, Message.WRONG_PASSWORD)
            else:
                messages.add_message(
                    request, messages.ERROR, Message.PASSWORD_NOT_MATCH)

        form = EditPasswordForm()
        return render(request, 'edit-password.html', {'form': form})
    else:
        messages.add_message(
            request, messages.ERROR, Message.PERMISSION_DENIED)
        return reverse('users:signin')


def reset_password(request):
    return password_reset(request, 'password-reset.html')
