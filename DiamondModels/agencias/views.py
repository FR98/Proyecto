from django.shortcuts import render
from agencias.models import Agencia
from modelos.models import Modelo

# Create your views here.

def lista_agencias(request):
	agencias = Agencia.objects.all()
	return render(request, 'agencias.html', {
		'agencias': agencias})

def detalle_agencia(request, agencia_pk):
	agencia = Agencia.objects.get(pk = agencia_pk)
	modelos = Modelo.objects.filter(agencia=agencia)
	return render(request, 'mi_agencia.html', {
		'agencia':agencia, 
		'modelos':modelos})