from django.shortcuts import render,  redirect, get_object_or_404
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

def  kom_create(request):
    """ name = models.CharField("Kompyuter nomi", max_length=100)
    model = models.CharField("Model", max_length=100)
    cpu = models.CharField("Protsessor (CPU)", max_length=100)
    ram = models.IntegerField("RAM (GB)")
    storage = models.CharField("Xotira turi va hajmi", max_length=100)
    screen_size = models.DecimalField("Ekran o‘lchami (dyuym)", max_digits=4, decimal_places=2)
    color = models.CharField("Rangi", max_length=50)
    price = models.DecimalField("Narxi (so‘m)", max_digits=12, decimal_places=2)
    discount_price = models.DecimalField("Chegirma narxi (so‘m)", max_digits=12, decimal_places=2, null=True, blank=True)
    image = models.ImageField("Rasm",upload_to= "kompyuter_App/",  null=True, blank=True)
    description = models.TextField("Tavsif", blank=True, null=True)
    created_at = models.DateTimeField("Qo‘shilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)"""
    kompyuter = Kompyuter()
    if  request.method == 'POST':
        kompyuter.name = request.POST['name']
        kompyuter.model = request.POST['model']
        kompyuter.cpu = request.POST['cpu']
        kompyuter.ram = request.POST['ram']
        kompyuter.storage = request.POST['storage']
        kompyuter.screen_size = request.POST['screen_size']
        kompyuter.color = request.POST['color']
        kompyuter.price = request.POST['price']
        kompyuter.discount_price = request.POST['discount_price']
        kompyuter.image = request.FILES['image']
        kompyuter.description = request.POST['description']
        kompyuter.save()
        return  redirect("kom_list")
    return render(request, 'kompyuter/kom_create.html', {'kompyuter': 'kompyuter'})

def  kom_update(request, id):
    kompyuter = Kompyuter.objects.get(id=id)
    if  request.method == 'POST':
        kompyuter.name = request.POST.get('name')
        kompyuter.model = request.POST.get('model')
        kompyuter.cpu = request.POST.get('cpu')
        kompyuter.ram = request.POST.get('ram')
        kompyuter.storage = request.POST.get('storage')
        kompyuter.screen_size = request.POST.get('screen_size')
        kompyuter.color = request.POST.get('color')
        kompyuter.price = request.POST.get('price')
        kompyuter.discount_price = request.POST.get('discount_price')
        image = request.FILES.get('image')
        if image:
            kompyuter.image = image
        kompyuter.description = request.POST.get('description')
        kompyuter.save()
        return redirect("kom_list")
    return  render(request,  'kompyuter/kom_update.html', {'kompyuter': kompyuter})


def  kom_delete(request, id):
    kompyuter = get_object_or_404(Kompyuter, id=id)
    if  request.method == 'POST':
        kompyuter.delete()
        return redirect("kom_list")
    return render(request,  'kompyuter/kom_delete.html', {'kompyuter': kompyuter})
