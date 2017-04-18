from django.db import models

# Create your models here.
class Modelo(models.Model):
	nombres = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 50)
	altura = models.FloatField(default= 0)
	peso = models.FloatField(default= 0)
	agencia = models.ForeignKey('agencias.Agencia')

	def __str__(self):
		return "%s %s - %s" % (
			self.nombres,
			self.apellidos,
			self.agencia)