from django.urls import path,include
from . import views

urlpatterns=[
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('register/',views.register,name='register'),
    path('userinfo/',views.userinfo,name='userinfo'),
    path('change_pwd/',views.change_pwd,name='change_pwd')
]