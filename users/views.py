from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

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
            return redirect('/users/register')
        
        if len(password) < 6:
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
                return HttpResponse("Success")
        except:
            return redirect('/users/register')
        
        return redirect('/users/register')
