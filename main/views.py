from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def home(request):
    return render(request, 'index.html')  # Usarás tu plantilla aquí


def component_view(request):
    return render(request, 'shop.html')

def details_view(request):
    return render(request, 'product-details.html')
