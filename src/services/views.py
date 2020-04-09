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

def services_detail(requset,id):
    services_detail = services.objects.get(id=id)
    template='services/detial.html'
    context= {
        'services_detail' : services_detail
    }
    return render(requset,template,context)