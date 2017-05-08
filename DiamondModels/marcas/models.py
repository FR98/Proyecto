from django.db import models

# Create your models here.

class Marca(models.Model):
	nombre = models.CharField(max_length=50)
	telefono = models.IntegerField(default=0)
	correo = models.CharField(max_length=50)

	def __str__(self):
		return "%s: %s, %s" % (
			self.nombre,
			self.telefono,
			self. correo)