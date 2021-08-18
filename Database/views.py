from django.shortcuts import redirect, render
from Database.models import EmpModel
from django.contrib import messages
from django.contrib.auth import authenticate, login

def Homedb(request):
    return render(request,'home.html')

def validate(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')     
        user = authenticate(request, username='admin@Ragavilan',password='rags27')
        if user is not None:
             redirect("ShowEmp")
        else:
            return render(request,"")
    else:
        return render(request,"")

    
def showEmp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{"data":showall})

def InsertEmp(request):
    if request.method=="POST":
        if request.POST.get('emp_name') and request.POST.get('emp_age') and  request.POST.get('emp_dept') and request.POST.get('emp_email') and request.POST.get('emp_gender'):
            saverecord=EmpModel()
            saverecord.emp_name=request.POST.get('emp_name')
            saverecord.emp_age=request.POST.get('emp_age')
            saverecord.emp_dept=request.POST.get('emp_dept')
            saverecord.emp_email=request.POST.get('emp_email')
            saverecord.emp_gender=request.POST.get('emp_gender')
            saverecord.save()
            messages.success(request,'Employee '+ saverecord.emp_name+ ' is saved Successfully..!')
            return render(request,'insert.html')
    else:
        return render(request,'insert.html')