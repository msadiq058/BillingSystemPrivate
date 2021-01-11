from django.contrib import admin

# Register your models here.
from .models import Firm,Entry

from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

class EntryAdmin(admin.ModelAdmin):
    list_display = ('firm_name','date','weight','quantity','making_type','remarks')
    list_filter = ('firm_name','date')

class FirmAdmin(admin.ModelAdmin):
    list_display = ('firm_name','gstin','date')

admin.site.register(Firm,FirmAdmin)
admin.site.register(Entry,EntryAdmin)