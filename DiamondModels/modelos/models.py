from django.db import models

# Create your models here.
class Modelo(models.Model):
	nombres = models.CharField(max_length = 50)
	grado = models.ForeignKey('grados.Grado')

	def __str__(self):
		return "%s %s - %s" % (
			self.nombres,
			self.apellidos,
			self.grado)