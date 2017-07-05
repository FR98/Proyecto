from django.db import models
from django.conf import settings

# Create your models here.

class Agencia(models.Model):
	nombre = models.CharField(max_length=50)
	telefono = models.IntegerField(default=0)
	correo = models.CharField(max_length=50)
	imagen = models.ImageField(null=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

	def __str__(self):
		return "%s: %s, %s" % (
			self.nombre,
			self.telefono,
			self.correo)