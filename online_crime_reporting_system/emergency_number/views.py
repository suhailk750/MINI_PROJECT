from django.shortcuts import render
from emergency_number.models import EmergencyNumber
# Create your views here.

def emnump(request):
    if request.method == "POST":
        ob=EmergencyNumber()
        ob.name=request.POST.get('username')
        ob.phone=request.POST.get('PHONE')
        ob.save()


    return render(request,'emergency_number/EMERGENCY_NO.HTML')

def emnumview(request):
    obj = EmergencyNumber.objects.all()
    context = {
        'x': obj
    }

    return render(request,'emergency_number/VIEW_EMERGENCY_NO.HTML',context)