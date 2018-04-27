from django.db import models

# Create your models here.

class Modelo(models.Model):
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField(default=0)
	altura = models.FloatField(default=0.0)
	peso = models.FloatField(default=0.0)
	telefono = models.IntegerField(default=0)
	agencia = models.ForeignKey('agencias.Agencia', on_delete=models.CASCADE)
	imagen = models.ImageField(null=True)


	def __str__(self):
		return "%s %s: %s --- %s" % (
			self.nombres,
			self.apellidos,
			self.telefono,
			self.agencia)
