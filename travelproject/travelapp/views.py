from django.shortcuts import render
from . models import Place, Team
# Create your views here.
from django.shortcuts import render
def home(request):
    obj=Place.objects.all()
    ob=Team.objects.all()
    return render(request,'index.html',{'result':obj,'res':ob})


