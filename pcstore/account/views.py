from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password != confirm_password:
            messages.error(request, "Паролі не співпадають.")
            return render(request, 'account/register.html')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        messages.success(request, "Реєстрація успішна!")
        return redirect('/account/register/')

    return render(request, 'account/register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Ви успішно вийшли з акаунту!")
    return redirect('/')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Вітаємо, {user.first_name}! Ви увійшли в систему.")
            return redirect('/')
        else:
            messages.error(request, "Невірне ім’я користувача або пароль.")
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')
