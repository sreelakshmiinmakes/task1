from django.shortcuts import render
from.models import place
from.models import human
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1 = human.objects.all()
    return render(request,"index.html",{'results':obj1,'result':obj},)





