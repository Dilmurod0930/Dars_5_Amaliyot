from django.shortcuts import render
from  .models import  Telefon

# Create your views here.
def  tele_list(request):
    telefons = Telefon.objects.all()
    context = {'telefons': telefons}
    return render(request, 'telefon/tele_list.html', context = context)

def  tele_info(request, id):
    telefon = Telefon.objects.get(id=id)
    context = {'telefon': telefon}
    return render(request, 'telefon/tele_info.html', context = context)

def  tele_create(request):
    telefon = Telefon()


def tele_update(request, id):
    telefon = Telefon.objects.get(id=id)