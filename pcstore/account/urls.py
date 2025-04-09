from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register_user, name='register_user'),
    path('profile/', views.profile_user, name='profile_user'),
    path('profile/change-password/', views.change_password, name='change_password'),
=======
    path('register/', views.register_user)
>>>>>>> 0c2974f (Add registration)
=======
=======
    path('login/', views.login_user),
>>>>>>> 7bd74d9 (Add login)
    path('logout/', views.logout),
    path('register/', views.register_user),
<<<<<<< HEAD
>>>>>>> 00e9245 (styling register)
=======
    path('profile/', views.profile_user),
    path('profile/change-password/', views.change_password)
>>>>>>> a3027a8 (Add user profile)
]
