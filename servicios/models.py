from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'
        verbose_name = 'SERVICIO'
        verbose_name_plural = 'SERVICIOS'