from django.shortcuts import render
from missing_person.models import MissingPerson
from django.core.files.storage import FileSystemStorage

# Create your views here.
def mipep(request):
    if request.method == "POST":
        ob=MissingPerson()
        ob.name=request.POST.get('username')
        ob.age=request.POST.get('age')
        ob.address=request.POST.get('addr')
        myfile=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        ob.photo=myfile.name
        ob.gender=request.POST.get('gndr')
        ob.save()

    return render(request,'missing_person/MISSING_PERSON.HTML')

def mipepolice(request):
    if request.method == "POST":
        ob=MissingPerson()
        ob.name=request.POST.get('username')
        ob.age=request.POST.get('age')
        ob.address=request.POST.get('addr')
        myfie=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(myfie.name,myfie)
        ob.photo=myfie.name
        ob.gender=request.POST.get('gndr')
        ob.save()

    return render(request,'missing_person/missing_person_police.html')

def mipeview(request):
    obj = MissingPerson.objects.all()
    context = {
        'x': obj
    }
    return render(request,'missing_person/VIEW_MISSING_PERSON.HTML',context)