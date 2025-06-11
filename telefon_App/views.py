from django.shortcuts import render
from  .models import  Telefon

# Create your views here.
def  tele_list(request):
    telefons = Telefon.objects.all()
    context = {'telefons': telefons}
    return render(request, 'telefon/tele_list.html', context = context)
