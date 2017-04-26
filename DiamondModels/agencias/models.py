from django.db import models

# Create your models here.
class Agencia(models.Model):
	nombre = models.CharField(max_length = 50)
	telefono = models.IntegerField(default = 0)

	def __str__(self):
		return "%s - %s" % (
			self.nombre,
			self.telefono)