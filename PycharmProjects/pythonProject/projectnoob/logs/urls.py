from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('',views.print_details,name='print_details'),
    
    # path('',views.requestData,name='requestData'),
]