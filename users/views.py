from django.shortcuts import render, redirect
from django.http import HttpResponse

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
        
        return HttpResponse("Pass")
