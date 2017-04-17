from django.shortcuts import render

# Create your views here.

def lista_agencias(request):
	agencias = Agencia.objects.all()
	return render(request, 'lista_agencias.html', {'agencias': agencias})