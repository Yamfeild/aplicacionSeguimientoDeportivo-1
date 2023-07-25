from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def futbol(request):
    return render(request, 'futbol.html')

def basquetbol(request):
    return render(request, 'basquetbol.html')

def ajedrez(request):
    return render(request, 'ajedrez.html')

def pingpong(request):
    return render(request, 'pingpong.html')
