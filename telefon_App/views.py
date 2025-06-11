from django.shortcuts import render, redirect , get_object_or_404
from  .models import  Telefon

""" name = models.CharField("Telefon nomi", max_length=100)
    model = models.CharField("Model", max_length=100)
    color = models.CharField("Rangi", max_length=50)
    discount_price = models.DecimalField("Chegirma narxi (so‘m)", max_digits=12, decimal_places=2, null=True,
                                         blank=True)
    price = models.DecimalField("Narxi (so‘m)", max_digits=12, decimal_places=2)
    storage = models.IntegerField("Xotira (GB)")
    ram = models.IntegerField("RAM (GB)")
    os = models.CharField("Operatsion tizim", max_length=50)
    image = models.ImageField("Rasm", upload_to='telefonlar/', null=True, blank=True)
    description = models.TextField("Tavsif", blank=True, null=True)
    created_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)
"""
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
    if  request.method == 'POST':
        telefon.name = request.POST.get('name')
        telefon.model = request.POST.get('model')
        color = request.POST.get('color')
        discount_price = request.POST.get('discount_price')
        price = request.POST.get('price')
        storage = request.POST.get('storage')
        ram = request.POST.get('ram')
        os = request.POST.get('os')
        image = request.POST.get('image')
        if image:
            telefon.image = image
        description = request.POST.get('description')
        telefon.save()

        return redirect('tele_list')
    return render(request, 'telefon/tele_info.html', context = {'telefon': telefon})


def tele_delete(request, id):
    telefon  = get_object_or_404(Telefon, id=id)
    if  request.method == 'POST':
        telefon.delete()
        return redirect('tele_list')
    return render(request, 'telefon/tele_delete.html', context = {'telefon': telefon})