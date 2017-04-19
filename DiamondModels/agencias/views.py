from django.shortcuts import render
from agencias.models import Agencia
from modelos.models import Modelo
from agencias.forms import AgenciaForm

# Create your views here.

def lista_agencias(request):
	agencias = Agencia.objects.all()
	formulario = AgenciaForm()
	return render(request, 'lista_agencias.html', {
		'agencias': agencias, 
		'agencia_form': formulario})

def detalle_agencia(request, agencia_pk):
	agencia = Agencia.objects.get(pk = agencia_pk)
	modelos = Modelo.objects.filter(agencia=agencia)
	return render(request, 'detalle_agencia.html', {
		'agencia':agencia, 
		'modelos':modelos})

def crear_agencia(request):
	formulario = AgenciaForm(data = request.POST)
	formulario.save()
	return redirect('/agencias/')