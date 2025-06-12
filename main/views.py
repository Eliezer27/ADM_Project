from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Componente

# Create your views here.
def home(request):
    return render(request, 'index.html')  # Usarás tu plantilla aquí


def component_view(request):
    return render(request, 'shop.html')

def details_view(request):
    return render(request, 'product-details.html')
#componentes
def detalle_componente(request, componente_id):
    try:
        componente = Componente.objects.prefetch_related('caracteristicas').get(id=componente_id)
    except Componente.DoesNotExist:
        componente = None  # O puedes hacer un render a una página de error personalizada

    return render(request, 'product-details.html', {'componente': componente})
