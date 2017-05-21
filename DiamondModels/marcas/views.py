from django.shortcuts import render
from marcas.models import Marca

# Create your views here.

def lista_marcas(request):
	marcas = Marca.objects.all()
	return render(request, 'marcas.html', {'marcas': marcas})

def detalle_marca(request, marca_pk):
	marca = Marca.objects.get(pk = marca_pk)
	return render(request, 'mi_marca.html', {
		'marca':marca})