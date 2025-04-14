"""
URL configuration for pcstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path, include
import components.views

urlpatterns = [
    path('components/', include('components.urls')),
    path('account/', include('account.urls')),
=======
from django.urls import path
=======
from django.urls import path, include
>>>>>>> 0c2974f (Add registration)
import components.views
import account.urls

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67d780e (add header)
=======
=======
    path('components/', include('components.urls')),
>>>>>>> ec58bea (add cpus page)
    path('account/', include('account.urls')),
>>>>>>> 0c2974f (Add registration)
    path('', components.views.landing, name="landing"),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
    path('order/', include('order.urls')),
    path('configurator/', include('configurator.urls')),
<<<<<<< HEAD
=======
>>>>>>> 4efcee2 (Add cart)
=======
    path('order/', include('order.urls')),
>>>>>>> c4c30a5 (Add order)
=======
>>>>>>> 394cf17 (add configurator)
]
