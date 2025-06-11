from django.shortcuts import render

# Create your views here.
def  main(request):
    return render(request, 'main.html')


def  kom_info(request):
    return render(request, 'kompyuter/kom_info.html')