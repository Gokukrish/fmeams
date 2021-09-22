from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from fmea_form.models import FmeaRegister
from fmea_form.models import FmeaProcess
from fmea_form.form import FmeaForm1, FmeaForm2
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html', )

# def register(request):
#     form=CreateUserForm()
#     if request.method=="POST":
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User created Sucessfully")
#             return redirect('login')
#     context={'form':form}
#     return render(request,'register.html',context)

@login_required
def fmeaProcessRegForm(request):
    form=FmeaForm1()
    if request.method=="POST":
        form=FmeaForm1(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Fmea created Successfully")
            return redirect('fmea')
        # process=request.POST.get('process')
        # preparedBy=request.POST.get('preparedBy')
        # responsible=request.POST.get('responsible')
        # date=request.POST.get('date')
        # revisedDate=request.POST.get('revisedDate')
    context={'form':form}
    return render(request,"fmeaForm.html",context)

@login_required
def fmeaProcess(request):
    form=FmeaForm2()
    if request.method=="POST":
        form=FmeaForm2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Fmea created Successfully")
            return render(request,"view_process.html",)
        # process=request.POST.get('process')
        # preparedBy=request.POST.get('preparedBy')
        # responsible=request.POST.get('responsible')
        # date=request.POST.get('date')
        # revisedDate=request.POST.get('revisedDate')
    context={'form':form}
    return render(request,"fmeaForm2.html",context)
    
@login_required
def view_process(request):
    context={}
    context["dataset"]=FmeaProcess.objects.all()
    return render(request,"view_process.html",context)
