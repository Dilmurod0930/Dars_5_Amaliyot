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
    if  request.method == 'POST':
        telefon.name = request.POST['name']
        telefon.model = request.POST['model']
        telefon.color = request.POST['color']
        telefon.discount_price = request.POST['discount_price']
        telefon.price = request.POST['price']
        telefon.storage = request.POST['storage']
        telefon.ram = request.POST['ram']
        telefon.os = request.POST['os']
        telefon.image = request.FILES['image']
        telefon.description = request.POST['description']
        telefon.save()
        return redirect('tele_list')
    return render(request, 'telefon/tele_create.html', context = {'telefon': 'telefon'})

def tele_update(request, id):
    telefon = Telefon.objects.get(id=id)
    if  request.method == 'POST':
        telefon.name = request.POST.get('name')
        telefon.model = request.POST.get('model')
        telefon.color = request.POST.get('color')
        telefon.discount_price = request.POST.get('discount_price')
        telefon.price = request.POST.get('price')
        telefon.storage = request.POST.get('storage')
        telefon.ram = request.POST.get('ram')
        telefon.os = request.POST.get('os')
        telefon.description = request.POST.get('description')
        telefon.image = request.FILES.get('image')
        image = request.POST.get('image')
        if image:
            telefon.image = image

        telefon.save()
        return redirect('tele_info', id= id)
    return render(request, 'telefon/tele_update.html', context = {'telefon': telefon})

def tele_delete(request, id):
    telefon  = get_object_or_404(Telefon, id=id)
    if  request.method == 'POST':
        telefon.delete()
        return redirect('tele_list')
    return render(request, 'telefon/tele_delete.html', context = {'telefon': telefon})