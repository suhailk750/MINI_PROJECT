from django.shortcuts import render
from login.models import Login

# Create your views here.
def loginp(request):
    return render(request,'login/login.html')