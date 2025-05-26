from django.views.generic import FormView
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from rest_framework import viewsets
from .serializer import ContactSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import yagmail

# Create your views here.

class ContactView(viewsets.ModelViewSet):
    queryset=Contact.objects.all().order_by('name')
    serializer_class=ContactSerializer
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset=Contact.objects.all().order_by('name')
    serializer_class=ContactSerializer    
    
def Registration(request):
    form=RegistrationForm(request.POST or None)
    if request.method=="POST":
        print("form was submitted")
        if form.is_valid():
            print("valid form ")
            form.save()
            user=form.save()
            login(request,user)
            return redirect("/gateway")
    data={"form":form,"title":"Register"}
    return render(request,"registration/registration.html",data)

def Dashboard(request, user_username):
    xl=User.objects.get(username=user_username)
    xa=AddPlan.objects.get(user=request.user)
    xg=SetUp.objects.get(user=request.user)
    xy=User.objects.filter(username=request.user.username)
    xf=AddPlan.objects.filter(user=request.user)
    xb=SetUp.objects.filter(user=request.user)
    xcount=User.objects.count()
    form=RegistrationForm(request.POST or None, instance=xl)
    forma = PlanForm(request.POST  or None, request.FILES or None, instance=xa)
    formp = SetUpForm(request.POST or None, instance=xg)
    if request.method=="POST":
        print("form was submitted")
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
        if forma.is_valid():
            print("valid form")
            forma.save()
            return redirect(f"/dashboard/{xl.username}")
        if formp.is_valid():
            print("valid form")
            formp.save()
            return redirect(f"/dashboard/{xl.username}")
    data={"users":xy,"usera":xl,"asera":xa,"gsera":xg,"count":xcount,"plans":xf,"account":xb,"form":form,"forma":forma,"formp":formp}
    return render(request,"billboard/dashboard.html",data)


def Gate(request):
    xy=User.objects.filter(username=request.user.username)
    form = ItemForm(initial={'user': request.user})
    forma = PlanForm(initial={'user': request.user})
    formp = SetUpForm(initial={'user': request.user})
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        forma = PlanForm(request.POST,request.FILES or None)
        formp = SetUpForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request submitted. Go to Step 4')
            return redirect("/gateway")
        if forma.is_valid():
            forma.save()
            messages.success(request, 'You are done with the process. View details by clicking DASHBOARD')
            return redirect("/gateway")
        if formp.is_valid():
            formp.save()
            messages.success(request, 'Request submitted. Go to Step 2')
            return redirect("/gateway")
    data={'users':xy, 'form': form, 'forma':forma, 'formp':formp}
    return render(request, 'billboard/gateway.html',data)   

def index(request):
    xy=User.objects.filter(username=request.user.username)
    if request.method=="POST":
        form=ContactForm(request.POST,request.FILES or None)
        forma = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            print("valid form ")
            print(request.POST.get('name')),
            user = 'keeshabillboard@gmail.com'
            app_password = 'xehcskzyjrlbbgbe' # a token for gmail
            subject = request.POST.get('name')
            from_email=request.POST.get('email')
            content= request.POST.get('options')
            to = [request.POST.get('email'), "keeshabillboard@gmail.com"]
            with yagmail.SMTP(user, app_password) as yag:
                yag.send(to, subject=subject, contents=content)
            print('Sent email successfully')
            form.save()
            return redirect("/billboard")
        if forma.is_valid():
            username=forma.cleaned_data.get('username')
            password=forma.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect(f"/dashboard/{username}")
            else:
                data={"form":form,"forma":forma,"dval":False}
                return render(request,"billboard/billboard.html",data)  
        else:
            data={"form":form,"forma":forma,"dval":False}
            return render(request,"billboard/billboard.html",data)
    forma=UserLoginForm()
    form=ContactForm()
    data={"users":xy,"form":form,"forma":forma,"dval":False}
    return render(request,"billboard/billboard.html",data)
