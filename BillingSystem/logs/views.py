
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Entry,Firm
from django import forms
from django.forms import ModelChoiceField
from .forms import NameForm
from .utils import generateExcel

def print_details(request):
    name =''
    # request.session.set_expiry(120)
    if request.method=='POST':
        form = NameForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            print(name,start_date,end_date)
            data = Entry.objects.filter(firm_name=name,date__range=[start_date,end_date])
            if(data.count()==0): print("No data found")
            else: generateExcel(data,name,start_date,end_date)
            
            # for i in data:
            #     print(str(i.date)+" "+str(i.firm_name)+" "+str(i.quantity)+" "+str(i.weight)+" "+str(i.remarks))
    else:
        form = NameForm
    return render(request,'logs/print_details.html',{'form':form})
