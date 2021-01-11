from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from .models import Entry,Firm
from django import forms
from django.forms import ModelChoiceField

class NameForm(forms.Form):
    name = ModelChoiceField(queryset=Firm.objects.all())