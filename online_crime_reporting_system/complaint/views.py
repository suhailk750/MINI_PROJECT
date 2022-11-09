from django.shortcuts import render
from complaint.models import Complaint
from django.core.files.storage import FileSystemStorage
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
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.photo = myfile.name
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


def response(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(c_id=idd)
        obj.reply=request.POST.get('response')
        obj.save()
        return viwresponse(request)
    return render(request,'complaint/reposnse.html')

def viwresponse(request):
    obj=Complaint.objects.filter(status='verified')
    context={
        'x':obj
    }
    return render(request,'complaint/view_response.html',context)



def reject(request,idd):
    ob=Complaint.objects.get(c_id=idd)
    ob.status='verified'
    ob.save()
    return cmpview(request)

def vem(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/view_emergency_response.html',context)

