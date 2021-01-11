
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Entry,Firm
from django import forms
from django.forms import ModelChoiceField
from .forms import NameForm

def index(request):
    form = NameForm()
    print(form)
    data = Entry.objects.filter(firm_name=form)
    for i in data:
        print(str(i.date)+" "+str(i.firm_name)+" "+str(i.quantity)+" "+str(i.weight)+" "+str(i.remarks))
    request.session.set_expiry(120)
    return render(request,'logs/index.html',{'form':form})
