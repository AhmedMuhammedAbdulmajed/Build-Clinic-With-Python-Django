from django.shortcuts import render
from .models import services
# Create your views here.
def services_list(requset):
    services_list = services.objects.all()
    template='services/list.html'
    context= {
        'services_list' : services_list
    }
    return render(requset,template,context)

def services_detail(requset):
    pass