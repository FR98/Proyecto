from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from marcas.models import Marca

# Create your views here.

def lista_marcas(request):
	marcas = Marca.objects.all()
	return render(request, 'marcas.html', {'marcas': marcas})

@login_required
def detalle_marca(request, marca_pk):
	marca = Marca.objects.get(pk = marca_pk)
	return render(request, 'mi_marca.html', {
		'marca':marca})

def login_marca(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		mi_marca = user.marca_set.all().first()
		return redirect("/marcas/" + str(mi_marca.pk))
	return redirect("/")

def logout_marca(request):
	logout(request)
	return redirect("/")