from django.shortcuts import render
from missing_person.models import MissingPerson

# Create your views here.
def mipep(request):
    if request.method == "POST":
        ob=MissingPerson()
        ob.name=request.POST.get('username')
        ob.age=request.POST.get('age')
        ob.address=request.POST.get('addr')
        ob.photo=request.POST.get('img')
        ob.gender=request.POST.get('gndr')
        ob.save()

    return render(request,'missing_person/MISSING_PERSON.HTML')

def mipeview(request):
    obj = MissingPerson.objects.all()
    context = {
        'x': obj
    }
    return render(request,'missing_person/VIEW_MISSING_PERSON.HTML',context)