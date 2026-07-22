
from django.shortcuts import render,redirect
from . import models
from .models import Staff, work_status_choices, area_choice


# Create your views here.
def staff_list(request):
    if request.method=='GET':
        staff_list=Staff.objects.all()
        return render(request,'staff/list.html',{'staff_list':staff_list})

def staff_add(request):
    if request.method=='GET':
        ctx={'gender_list':models.gender_choice,
             'staff_type_list':models.staff_type_choice,
             'work_status_list':work_status_choices,
             'area_choice_list':area_choice
             }
        return render(request,'staff/add.html',ctx)
    if request.method=='POST':
        Staff.objects.create(name=request.POST.get('name'),
        gender=request.POST.get('gender'),
        birth=request.POST.get('birth'),
        id_number=request.POST.get('id_number'),
        staff_type=request.POST.get('staff_type'),
        work_status=request.POST.get('work_status'),
        work_area=request.POST.get('work_area'))
        return redirect('staff_list')

