from django.shortcuts import render, HttpResponse, redirect
from ieeewie.models import Newsform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.template.loader import render_to_string


#from ieeewie.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER

# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')

def newsletters(request):
    #return HttpResponse("This is my home page")
    return render(request, 'newsletters.html')

def newsletteredition(request):
    #return HttpResponse("This is my home page")
    return render(request, 'newsletteredition.html')

def newsletterform(request):
    #return HttpResponse("This is my home page")
    if request.method=="POST":
    
        month=request.POST['month']
        year=request.POST['year']
        glossary=request.POST['glossary']
        headlines=request.POST['headlines']
        timeline=request.POST['timeline']
        womenintech=request.POST['womenintech']
        learning=request.POST['learning']
        myth=request.POST['myth']
        gizmo=request.POST['gizmo']
        summary=request.POST['summary']
        faq=request.POST['faq']
        spot=request.POST['spot']
        performer=request.POST['performer']
        image_head=request.POST['image_head']
        #pdf=request.POST['timeline']
        

        newsdata = Newsform(month=month, year=year, glossary=glossary, headlines=headlines, timeline=timeline, womenintech=womenintech, learning=learning, myth=myth, gizmo=gizmo, summary=summary, faq=faq, image_head=image_head, spot=spot, performer=performer)  

        newsdata.save()
        
        messages.success(request, "Newsletter Added Succesfully")
        
    #return render(request,"foodsordernow.html",{"Orders":adduserdata})
    #return render(request,"adduser.html")
    #return render(request,"adduser.html",{"Us":adduserorder})

    return render(request, 'newsletterform.html')

def blogs(request):
    #return HttpResponse("This is my home page")
    return render(request, 'blogs.html')

def page404(request):
    #return HttpResponse("This is my home page")
    return render(request, 'page404.html')

def registrationclosed(request):
    #return HttpResponse("This is my home page")
    return render(request, 'registrationclosed.html')
