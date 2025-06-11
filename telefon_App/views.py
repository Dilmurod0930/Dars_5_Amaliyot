from django.shortcuts import render
from  .models import  Telefon

# Create your views here.
def  tele_info(request):
    telefons = Telefon.objects.all()
    context = {'telefons': telefons}
    return render(request, 'telefon/tele_info.html', context = context)
