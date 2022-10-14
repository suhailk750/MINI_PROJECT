from django.shortcuts import render
from police_registration.models import PoliceRegistration

# Create your views here.
def preg(request):
    if request.method == "POST":
        ob=PoliceRegistration()
        ob.name=request.POST.get('name')
        ob.username=request.POST.get('username')
        ob.password=request.POST.get('psw')
        ob.location=request.POST.get('loc')
        ob.status='pending'
        ob.save()
    return render(request,'police_registration/POLICE_REGISTRATION.HTML')

def mpolice(request):
    obj = PoliceRegistration.objects.all()
    context = {
        'x': obj
    }
    return render(request,'police_registration/manage_police.html',context)

def approve(request,idd):
    ob=PoliceRegistration.objects.get(pr_id=idd)
    ob.status='approve'
    ob.save()
    return mpolice(request)

def reject(request,idd):
    ob=PoliceRegistration.objects.get(pr_id=idd)
    ob.status='reject'
    ob.delete()
    return mpolice(request)