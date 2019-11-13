from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PersonForm, PassportForm
from .forms import PersonModel,PassportModel


def addPE(request):
    return render(request,"addPE.html",{"form":PersonForm()})


def savePE(request):
     aadhar=request.POST.get("aadhar")
     name = request.POST.get("pname")
     contact = request.POST.get("contact")
     adr = request.POST.get("address")
     PersonModel(aadhar=aadhar,pname=name,contact=contact,address=adr).save()
     messages.success(request,"person details are saved")
     return redirect('main')


def viewPE(request):
    return render(request,"viewPE.html",{"data":PersonModel.objects.all()})


def addPAS(request):
    return render(request,"addPAS.html",{"form":PassportForm()})


def savePAS(request):
    no=request.POST.get("pno")
    details = request.POST.get("p_details")
    PassportModel(pno=no,p_details_id=details).save()
    messages.success(request,"passport details are saved")
    return redirect('main')


def viewPAS(request):
    return render(request,"viewPAS.html",{"data":PassportModel.objects.all()})