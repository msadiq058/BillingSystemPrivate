from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
from .models import Entry,Firm
from django import forms
from django.forms import ModelChoiceField , widgets , SelectDateWidget
from django.forms.fields import *
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

class NameForm(forms.Form):
    queryset = Firm.objects.all()
    name = ModelChoiceField(queryset=queryset)
    start_date = DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    
    def clean(self):
        # cleaned_data = super().clean()
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        
        today_date = date.today()

        if start_date>today_date and end_date>today_date:
            self._errors['start_date']=[u"Start and end date can't exceed todays's date." ]
            # raise forms.ValidationError(_("Start and end date can't exceed today's date."))
        elif start_date>today_date:
            # raise forms.ValidationError(_("Start date can't exceed today's date."))
            self._errors['start_date']=[u"Start date can't exceed today's date." ]
        elif end_date > today_date:
            self._errors['start_date']=[u"End date can't exceed today's date." ]
            # raise forms.ValidationError(_("End date can't exceed today's date."))
        elif(end_date < start_date):
            self._errors['start_date']=[u"End date must be greater than start date." ]
            # raise ValidationError(_("Start date must be greater than today's date."))
        
        # return self.cleaned_data