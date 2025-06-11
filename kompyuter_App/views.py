from django.shortcuts import render
from .models import Kompyuter
# Create your views here.
def  main(request):
    return render(request, 'main.html')


def  kom_list(request):
    kompyuters = Kompyuter.objects.all()
    context = {'kompyuters': kompyuters}
    return render(request, 'kompyuter/kom_list.html', context = context)