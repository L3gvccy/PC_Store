from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout),
    path('register/', views.register_user),
    path('profile/', views.profile_user),
    path('profile/change-password/', views.change_password)
]
