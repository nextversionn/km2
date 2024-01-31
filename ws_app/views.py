from django.shortcuts import render

# Create your views here.

def Home(req):
    return render(req, 'home.html')

def About(req):
    return render(req, 'about.html')

def Service(req):
    return render(req, 'service.html')

def Contact(req):
    return render(req, 'contact.html')