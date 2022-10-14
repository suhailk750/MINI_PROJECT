from django.shortcuts import render
from complaint.models import Complaint
# Create your views here.
def cmp(request):
    if request.method=="POST":
        ob=Complaint()
        ob.complaint=request.POST.get('crimereport')
        ob.user_id=1
        ob.date=request.POST.get('date')
        ob.location=request.POST.get('location')
        ob.name=request.POST.get('name')
        ob.phone=request.POST.get('PHONE')
        ob.photo=request.POST.get('img')
        ob.time=request.POST.get('time')
        ob.reply='pending'
        ob.status="pending"
        ob.save()

    return render(request,'complaint/COMPLAINT.HTML')

def cmpview(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/VIEWCOMP.HTML',context)

def reject(request,idd):
    ob=Complaint.objects.get(c_id=idd)
    ob.status='verify'
    ob.save()
    return cmpview(request)