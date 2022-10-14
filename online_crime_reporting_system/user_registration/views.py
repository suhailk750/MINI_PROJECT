from django.shortcuts import render
from user_registration.models import UserRegistration

# Create your views here.
def ureg(request):
    if request.method == "POST":
        ob=UserRegistration()
        ob.name=request.POST.get('name')
        ob.address=request.POST.get('adr')
        ob.phone=request.POST.get('phone')
        ob.age=request.POST.get('age')
        ob.gender=request.POST.get('gndr')
        ob.email=request.POST.get('mail')
        ob.password=request.POST.get('username')
        ob.username=request.POST.get('Password')
        ob.save()
    return render(request,'user_registration/USER_REGISTRATION.html')