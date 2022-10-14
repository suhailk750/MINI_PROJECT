from django.shortcuts import render
from criminal_list.models import CriminalList

# Create your views here.
def crlp(request):
    if request.method == "POST":
        ob=CriminalList()
        ob.photo=request.POST.get('img')
        ob.name=request.POST.get('username')
        ob.location=request.POST.get('LOCATION')
        ob.age=request.POST.get('age')
        ob.save()
    return render(request,'criminal_list/CRIMINAL_LIST.HTML')

def crlview(request):
    obj=CriminalList.objects.all()
    context = {
        'x': obj
    }
    return render(request,'criminal_list/VIEW_CRIMINAL_LIST.HTML',context)