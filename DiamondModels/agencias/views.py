from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
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

def login_agencia(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		mi_agencia = user.agencia_set.all().first()
		return redirect("/agencias/" + str(mi_agencia.pk))
	return redirect("/")

def logout_agencia(request):
	return redirect("/")