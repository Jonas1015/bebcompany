from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})


def products(request):
    return render(request, 'main/products.html', {})


def about(request):
    return render(request, 'main/about.html', {})


def contact(request):
    return render(request, 'main/contact.html', {})
