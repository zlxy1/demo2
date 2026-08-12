from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('change_pwd/', views.change_pwd, name='change_pwd'),
    path('upload/', views.upload_avatar, name='upload'),
    path('user_manage/', views.user_manage, name='user_manage'),
    path('user_edit/<int:uid>', views.user_edit, name='user_edit'),
    path('user_delete/<int:uid>', views.user_delete, name='user_delete'),
    path("user_add/", views.user_add, name="user_add"),

]
