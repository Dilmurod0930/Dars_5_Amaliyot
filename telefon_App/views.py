from django.shortcuts import render

# Create your views here.
def  tele_info(request):
    return render(request, 'telefon/tele_info.html')
