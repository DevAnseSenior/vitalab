from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm_password')

        if not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'The passwords entered do not match')
            return redirect('/users/register')
        
        if len(password) < 6:
            messages.add_message(request, constants.WARNING, 'Password must have 6 or more digits')
            return redirect('/users/register')
        
        try:
            existing_user = User.objects.filter(username=username).exists()
            if not existing_user:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                messages.add_message(request, constants.SUCCESS, 'User registered successfully')
            else:
                messages.add_message(request, constants.ERROR, 'Error, username already registered')
        except:
            messages.add_message(request, constants.ERROR, 'Internal system error, contact an administrator')
            return redirect('/users/register')
        
        return redirect('/users/register')
