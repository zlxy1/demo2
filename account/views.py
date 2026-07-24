from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
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
    if request.method == "POST":
        logout(request)
    return redirect('login_view')
