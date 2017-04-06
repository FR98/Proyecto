from django.db import models

# Create your models here.
class Agencia(models.Model):
	nombre = models.CharField(max_length = 50)
	telefono = models.IntegerField(max_length = 20)

	def __str__(self):
		return "%s %s - %s" % (
			self.nombres,
			self.telefono)