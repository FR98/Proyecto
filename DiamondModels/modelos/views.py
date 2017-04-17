from django.shortcuts import render

# Create your views here.

def lista_modelos(request):
	modelos = Modelo.objects.all()
	return render(request, 'lista_modelos.html', {'modelos': modelos})