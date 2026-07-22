from . import views
from django.urls import path

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('staff/list', views.staff_list, name='staff_list'),
    path('staff/add', views.staff_add, name='staff_add')

]
