from django.shortcuts import render
from .models import Kompyuter
# Create your views here.
def  main(request):
    return render(request, 'main.html')


def  kom_list(request):
    kompyuters = Kompyuter.objects.all()
    context = {'kompyuters': kompyuters}
    return render(request, 'kompyuter/kom_list.html', context = context)

def kom_info(request,  id):
    kompyuter = Kompyuter.objects.get(id=id)
    context = {'kompyuter': kompyuter}
    return render(request, 'kompyuter/kom_info.html', context = context)