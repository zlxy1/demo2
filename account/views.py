from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile, DEP_CHOICE
from functools import wraps
from django.shortcuts import render


def admin_required(view_func):
    @wraps(view_func)
    def wrap(request, *a, **b):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        if not (profile.is_admin or request.user.is_superuser):
            return redirect('staff_list')
        return view_func(request, *a, **b)
    return wrap

def login_view(request):
    if request.user.is_authenticated:
        return redirect('staff_list')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('staff_list')
        else:
            msg = '用户名或密码错误'
            return render(request, 'account/login.html', {'msg': msg})
    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


def register(request):
    # 已登录用户直接跳转主页，return终止代码
    if request.user.is_authenticated:
        return redirect('staff_list')

    msg = ''
    if request.method == "POST":
        # 设置默认空字符串，防止None调用strip报错
        username = request.POST.get('username', "").strip()
        dep = request.POST.get('dep', '')
        password1 = request.POST.get('password1', "")
        password2 = request.POST.get('password2', "")

        # 1.优先判断用户名非空
        if not username:
            msg = '用户名为空，无法注册'
        elif not dep:
            msg = '请选择您所在的科室'
        # 2.校验两次密码是否一致
        elif password1 != password2:
            msg = '两次输入的密码不一致'
        # 3.校验用户名是否被占用
        elif User.objects.filter(username=username).exists():
            msg = '用户名已存在！'
        # 全部校验通过，创建普通用户
        else:
            user = User.objects.create_user(username=username, password=password1)
            UserProfile.objects.create(
                user=user,
                is_admin=False,  # 注册默认普通用户
                dep=dep)
            # 跳转登录页，填入路由name别名 login
            return redirect('login_view')

    # GET请求 或 校验失败，返回注册页面并携带提示文字
    return render(request, 'account/register.html', {'msg': msg, 'dep': DEP_CHOICE})


@login_required
def userinfo(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    is_admin = profile.is_admin
    is_super=request.user.is_superuser
    return render(request, 'account/userinfo.html', {'is_admin': is_admin,"is_super":is_super})


@login_required
def change_pwd(request):
    msg = ''
    if request.method == 'POST':
        old_pwd = request.POST.get('old_pwd', '')
        new_pwd1 = request.POST.get('new_pwd1', '')
        new_pwd2 = request.POST.get('new_pwd2', '')

        # 新增：判断输入框不能为空
        if not old_pwd or not new_pwd1 or not new_pwd2:
            msg = '所有输入框不能为空'
        elif not check_password(old_pwd, request.user.password):
            msg = '原密码输入错误'
        elif new_pwd1 != new_pwd2:
            msg = '两次新密码输入不一致'
        elif len(new_pwd1) < 8:
            msg = '密码长度至少8位'
        else:
            # 修改密码并加密存储
            user = request.user
            user.set_password(new_pwd1)
            user.save()
            # 更新会话，无需重新登录
            update_session_auth_hash(request, user)
            msg = '密码修改成功！'

    # 必须把msg到上下文字典传给html页面
    return render(request, 'account/change_pwd.html', {'msg': msg})


@login_required
def upload_avatar(request):
    msg = ''
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        avatar = request.FILES.get('avatar', '')
        nickname = request.POST.get('nickname', '')
        dep = request.POST.get('dep', '')
        if not avatar:
            msg = '请上传头像'
        else:
            profile.avatar = avatar
            profile.nickname = nickname
            profile.dep = dep
            profile.save()
            return redirect('userinfo')
    return render(request, 'account/upload.html', {'msg': msg, 'dep': DEP_CHOICE,'profile':profile})
