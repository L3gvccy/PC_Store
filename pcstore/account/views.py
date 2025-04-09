from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email,first_name = first_name,last_name = last_name)
        user.save()

        return redirect('/account/register/') 
    
    return render(request, 'account/register.html')
