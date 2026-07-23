from . import views
from django.urls import path

from .views import staff_add

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('staff/list', views.staff_list, name='staff_list'),
    path('staff/add', views.staff_add, name='staff_add'),
    path('staff/del/<int:pk>', views.staff_del, name='staff_del'),
    path('staff/edit/<int:pk>',views.staff_edit,name='staff_edit')

]
