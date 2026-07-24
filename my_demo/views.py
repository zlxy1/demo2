from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Staff, work_status_choices, area_choice
@login_required
def staff_add(request):
    if request.method == 'GET':
        ctx = {'gender_list': models.gender_choice,
               'staff_type_list': models.staff_type_choice,
               'work_status_list': work_status_choices,
               'area_choice_list': area_choice
               }
        return render(request, 'staff/add.html', ctx)
    if request.method == 'POST':
        Staff.objects.create(name=request.POST.get('name'),
                             gender=request.POST.get('gender'),
                             birth=request.POST.get('birth'),
                             id_number=request.POST.get('id_number'),
                             staff_type=request.POST.get('staff_type'),
                             work_status=request.POST.get('work_status'),
                             work_area=request.POST.get('work_area'))
        return redirect('staff_list')

@login_required
def staff_del(request, pk):
    staff_del = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        staff_del.delete()
        return redirect('staff_list')

@login_required
def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    ctx1 = {'gender_list': models.gender_choice,
            'staff_type_list': models.staff_type_choice,
            'work_status_list': work_status_choices,
            'area_choice_list': area_choice,
            'staff': staff
            }
    if request.method == 'GET':
        return render(request, 'staff/edit.html', ctx1)
    else:
        staff.name=request.POST.get('name')
        staff.gender = request.POST.get('gender')
        staff.birth = request.POST.get('birth')
        staff.id_number = request.POST.get('id_number')
        staff.staff_type = request.POST.get('staff_type')
        staff.work_status = request.POST.get('work_status')
        staff.work_area = request.POST.get('work_area')
        staff.save()
        return redirect('staff_list')

@login_required
def staff_list(request):
    qs=Staff.objects.all()
    serach_name=request.GET.get('name','')
    serach_work_area=request.GET.get('work_area','')
    if serach_name:
        qs=qs.filter(name__icontains=serach_name)
    if serach_work_area:
        qs=qs.filter(name__icontains=serach_work_area)
    return render(request,'staff/list.html',{'staff_list':qs})

