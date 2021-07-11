from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    path('print_details',views.print_details,name='print_details'),
    path('',views.home_page,name='home_page'),
    
    # path('',views.requestData,name='requestData'),
]