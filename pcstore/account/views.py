from django.contrib.auth.models import User
from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
=======
>>>>>>> 0c2974f (Add registration)

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
<<<<<<< HEAD
<<<<<<< HEAD
        confirm_password = request.POST['confirm_password']
=======
>>>>>>> 0c2974f (Add registration)
=======
        confirm_password = request.POST['confirm_password']
>>>>>>> 64a115f (update register)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

<<<<<<< HEAD
<<<<<<< HEAD
        if password != confirm_password:
            messages.error(request, "Паролі не співпадають.")
            return
=======
        if password != confirm_password:
            messages.error(request, "Паролі не співпадають.")
            return render(request, 'account/register.html')
>>>>>>> 64a115f (update register)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
<<<<<<< HEAD
        user.save()

        messages.success(request, "Реєстрація успішна!")
        return redirect('/account/login/')

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

@login_required
def profile_user(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        messages.success(request, "Інформацію оновлено успішно!")
        return redirect('/account/profile/')

    return render(request, 'account/profile.html', {'user': request.user})

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, "Старий пароль введено невірно.")
        elif new_password != confirm_password:
            messages.error(request, "Нові паролі не співпадають.")
        else:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Зберегти сесію
            messages.success(request, "Пароль успішно змінено.")
            return redirect('/account/profile/')

    return render(request, 'account/change_password.html')
=======
        user = User.objects.create_user(username=username, password=password, email=email,first_name = first_name,last_name = last_name)
=======
>>>>>>> 64a115f (update register)
        user.save()

        messages.success(request, "Реєстрація успішна!")
        return redirect('/account/register/')

    return render(request, 'account/register.html')
<<<<<<< HEAD
>>>>>>> 0c2974f (Add registration)
=======

>>>>>>> db35cdc (Update registration)
