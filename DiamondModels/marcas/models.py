from django.db import models

class Marca(models.Model):
	nombre = models.CharField(max_length = 50)
	telefono = models.IntegerField(default = 0)
	
	def __str__(self):
		return "%s %s - %s" % (
			self.nombres,
			self.telefono)