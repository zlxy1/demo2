import io
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import content_disposition_header
from openpyxl.workbook import Workbook
from . import models
from .models import Staff, work_status_choices, area_choice
from django.core.paginator import Paginator

def excel_export(data_list):
    wb=Workbook()
    ws=wb.active
    ws.title='员工信息表'
    row=['姓名','性别','出生日期','身份证号','人员类型','在职状态','所属科室']
    ws.append(row)
    for item in data_list:
        ws.append([item.name,item.get_gender_display(),item.birth,item.id_number,item.staff_type,item.work_status,item.work_area])
    buffer=io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    wb.close()
    return buffer

def staff_filter(request,qs):
    search_name=request.GET.get('name','')
    search_work_area=request.GET.get('work_area','')
    if search_name:
        qs = qs.filter(name__icontains=search_name)
    if search_work_area:
        qs = qs.filter(work_area__icontains=search_work_area)
    return qs

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
    qs=Staff.objects.all().order_by('id')
    qs=staff_filter(request,qs)
    paginator = Paginator(qs, 8)
    pag_num = request.GET.get('page', 1)
    page_data = paginator.get_page(pag_num)
    return render(request,'staff/list.html',{'staff_list':page_data})

@login_required()
def staff_export(request):
    qs = Staff.objects.all().order_by('id')
    qs = staff_filter(request, qs)
    buf=excel_export(qs)
    response=HttpResponse(buf.getvalue(),content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="员工信息表.xlsx"'
    return response