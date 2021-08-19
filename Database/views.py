from django.shortcuts import redirect, render
from Database.models import EmpModel
from Database.models import Empdept
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from Database.forms import Empforms, Deptforms

@csrf_exempt
def Homedb(request):
    return render(request,'home.html')
    
def showEmp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{"data":showall})

def showDept(request):
    showdept=Empdept.objects.all()
    return render(request,'dept.html',{"data":showdept})

def InsertEmp(request):
    if request.method=="POST":
        if request.POST.get('emp_name') and request.POST.get('emp_age') and  request.POST.get('emp_dept') and request.POST.get('emp_email') and request.POST.get('emp_gender') and request.POST.get('emp_salary'):
            saverecord=EmpModel()
            saverecord.emp_name=request.POST.get('emp_name')
            saverecord.emp_age=request.POST.get('emp_age')
            saverecord.emp_dept=request.POST.get('emp_dept')
            saverecord.emp_email=request.POST.get('emp_email')
            saverecord.emp_gender=request.POST.get('emp_gender')
            saverecord.emp_gender=request.POST.get('emp_salary')
            saverecord.save()
            messages.success(request,'Employee '+ saverecord.emp_name+ ' is saved Successfully..!')
            return render(request,'insert.html')
    else:
        return render(request,'insert.html')

def EditEmp(request,id):
    editobj=EmpModel.objects.get(id=id)
    return render(request,'edit.html',{"EmpModel":editobj})

def UpdateEmp(request,id):
    updateEmp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=updateEmp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully.!!')
        return render(request,'edit.html',{"EmpModel":updateEmp})

def DelEmp(request,id):
    delemp=EmpModel.objects.get(id=id)
    delemp.delete()
    showdata=EmpModel.objects.all()
    return render(request, "index.html",{"data":showdata})

def InsertDept(request):
    if request.method=="POST":
        if request.POST.get('dept_name') and request.POST.get('dept_hod'): 
            saverecord=Empdept()
            saverecord.dept_name=request.POST.get('dept_name')
            saverecord.dept_hod=request.POST.get('dept_hod')
            saverecord.save()
            messages.success(request,'Department '+ saverecord.dept_name+ ' is saved Successfully..!')
            return render(request,'insert_dept.html')
    else:
        return render(request,'insert_dept.html')


def Editdept(request,id):
    editobj=Empdept.objects.get(id=id)
    return render(request,'edit_dept.html',{"Empdept":editobj})

def Deldept(request,id):
    deldept=Empdept.objects.get(id=id)
    deldept.delete()
    showdata=Empdept.objects.all()
    return render(request, "dept.html",{"data":showdata})

def UpdateEmp(request,id):
    updatedept=Empdept.objects.get(id=id)
    form=Deptforms(request.POST,instance=updatedept)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully.!!')
        return render(request,'edit_dept.html',{"Empdept":updatedept})
