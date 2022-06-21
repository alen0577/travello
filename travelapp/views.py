from django.shortcuts import render
from .models import Place,Blog


# Create your views here.
def home(request):
    obj = Place.objects.all()
    obj1 = Blog.objects.all()

    return render(request, 'index.html', {"results": obj, "blogs": obj1})


def addition(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    num3 = num1 + num2
    return render(request, 'result.html', {'sum': num3})
