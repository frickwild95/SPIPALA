from django.db import models
from servicios.models import *
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.


class TypeReport(models.Model):
    name = models.CharField('Nombre del reporte' , max_length=50)

    def __str__(self):
        return self.name

    def imprimir (self):
        return mark_safe(u'<a href="/imprimir" target="_blank">imprimir</href>')
    imprimir.short_description = 'imprimir'


report_status = [ (1, 'En proceso'), (2, 'Completado') ]


class Report(models.Model):
    type = models.ForeignKey(TypeReport, on_delete=models.CASCADE, help_text='Seleccione un tipo de servicio')
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField('Nombre completo', max_length=100, help_text = 'Ejemplo: Juan Pérez')
    telefono = models.CharField('Telefono', max_length = 50)
    residencia = models.CharField('Lugar de residencia', max_length=100, help_text='¿Cúal es la dirección de su hogar?')
    referencia = models.CharField('Referencia del lugar', max_length=100, help_text='Ejemplo: A unos pasos de tienda "La Vencedora"')
    descripcion = models.TextField('Descripción del problema', max_length=100, help_text='Breve descripción del problema a reportar')
    foto = models.ImageField(upload_to='img/%Y/%m/%d', max_length=255, blank=True, null=True, help_text='Adjunte una imagen del problema o del lugar donde está el problema')
    ubicacion = models.CharField('Ubicación', max_length=100, blank=True, help_text='Aquí se cargan sus coordenadas para ubicar el problema, asegurese de estar en el lugar del problema')
    status = models.IntegerField(
        null=False, blank=False,
        choices=report_status,
        default=1
    )

    def __str__(self):
        return self.usuario

    def comprobante (self):
        return mark_safe(u'<a href="/comprobante/?id=%s" target="_blank">comprobante</a>' % self.id)
    comprobante.short_description = 'comprobante'



# class Reporte (models.Model):
#     fecha = models.DateTimeField(auto_now_add=True)
#     usuario = models.CharField('Nombre completo', max_length=100, help_text = 'Juan Pérez')
#     residencia = models.CharField('Lugar de residencia', max_length=100)
#     referencia = models.TextField('Referencia del lugar', max_length=100)
#     #ubicacion = models.CharField('Ubicación', max_length=100, blank=True)
#     ubicacion = models.TextField('Geo', blank=True, null=True)
#     # ubicacion = geomodels.PointField(srid=4326, blank=True,)
#     descripcion = models.TextField('Descripción del problema', max_length=100)
#     foto = models.ImageField(upload_to='img/%Y/%m/%d', max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.usuario
#
#     class Meta:
#         abstract = True
#
# class Reporte_AguaPotable(Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_aguapotable'
#         verbose_name = 'REPORTE DE AGUA POTABLE'
#         verbose_name_plural = 'REPORTES DE AGUA POTABLE'
#
# class Reporte_Drenajes (Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_drenajes'
#         verbose_name = 'REPORTE DE DRENAJES'
#         verbose_name_plural = 'REPORTES DE DRENAJES'
#
# class Reporte_AlumbradoPublico(Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_alumbradopublico'
#         verbose_name = 'REPORTE DE ALUMBRADO PUBLICO'
#         verbose_name_plural = 'REPORTES DE ALUMBRADO PUBLICO'
#
# class Reporte_Cementerio(Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_cementerio'
#         verbose_name = 'REPORTE DE CEMENTERIO'
#         verbose_name_plural = 'REPORTES DE CEMENTERIO'
#
# class Reporte_Mercado(Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_mercado'
#         verbose_name = 'REPORTE DE MERCADO'
#         verbose_name_plural = 'REPORTES DE MERCADO'
#
# class Reporte_TrendeAseo(Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_trendeaseo'
#         verbose_name = 'REPORTE DE TREN DE ASEO'
#         verbose_name_plural = 'REPORTES DE TREN DE ASEO'
#
# class Reporte_TransportePublico(Reporte):
#     servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)
#
#     def __str__(self):
#         return str(self.servicio)
#
#     class Meta:
#         db_table = 'reporte_transportepublico'
#         verbose_name = 'REPORTE DE TRANSPORTE PUBLICO'
#         verbose_name_plural = 'REPORTES DE TRANSPORTE PUBLICO'
#    LOAN_STATUS = (
#        ('g', 'Gestionado'),
#        ('p', 'Por gestionar'),
#
#    )

#    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

  #  class Meta:
  #      ordering = ["due_back"]

# class PhoneType (models.Model):
#     type = models.CharField('Tipo', max_length=50, help_text='Ingrese el tipo de número telefonico ya sea Celular, Residencial, Laboral, etc.')

#     def __str__(self):
#         return self.type

#     class Meta:
#         db_table = 'phonetype'
#         verbose_name = 'Tipo de número de teléfono'
#         verbose_name_plural = 'Tipos de números de teléfonos'
#         unique_together = ['type'] #no puede existir otra tipos de números iguales


# class PhoneNumber (models.Model):
#     client = models.ForeignKey(Client, on_delete = models.CASCADE, verbose_name = 'Cliente')
#     phonetype = models.ForeignKey(PhoneType, on_delete = models.CASCADE, verbose_name = 'Tipo de número telefónico')
#     number = models.PositiveIntegerField ('Número de Teléfono', help_text='Solo ingresar números')

#     def __str__(self):
#         cadena = "{0} {1} {2}"
#         return cadena.format(self.client, self.phonetype, self.number)

#     def ClientName (self) :
#         return self.client.nombrecompleto()

#     class Meta:
#         db_table = 'phonenumber'
#         verbose_name = 'Número de teléfono'
#         verbose_name_plural = 'Números de teléfono'
#         unique_together = ['number']