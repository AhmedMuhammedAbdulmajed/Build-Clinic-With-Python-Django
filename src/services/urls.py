from django.urls import path
from . import views
app_name='services'
urlpatterns = [
    path('', views.services_list , name='services_list'),
     path('<int:id>', views.services_detail , name='services_detail'),
]
