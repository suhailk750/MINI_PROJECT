from django.shortcuts import render
from criminal_list.models import CriminalList
from django.core.files.storage import FileSystemStorage

# Create your views here.
def crlp(request):
    if request.method == "POST":
        ob=CriminalList()
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.photo = myfile.name
        ob.name=request.POST.get('username')
        ob.location=request.POST.get('LOCATION')
        ob.age=request.POST.get('age')
        ob.save()
    return render(request,'criminal_list/CRIMINAL_LIST.HTML')

def crlistp(request):
    if request.method == "POST":
        ob=CriminalList()
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.photo=myfile.name
        ob.name=request.POST.get('username')
        ob.location=request.POST.get('LOCATION')
        ob.age=request.POST.get('age')
        ob.save()
    return render(request,'criminal_list/criminal_list_police.html')




def crlview(request):
    obj=CriminalList.objects.all()
    context = {
        'x': obj
    }
    return render(request,'criminal_list/VIEW_CRIMINAL_LIST.HTML',context)