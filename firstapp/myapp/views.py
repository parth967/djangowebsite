from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
import datetime 
from myapp.form import UserForm

# Create your views here.
def form(request):
    user=UserForm()
    return render(request,"form.html",{'form':user})
    
def index(request):
    template=loader.get_template('index.html')
    name={
        'name':'parth',
        'enroll':'151240116028'
        }

    return HttpResponse(template.render(name))
