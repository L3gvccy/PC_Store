from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req, 'components/landing.html')