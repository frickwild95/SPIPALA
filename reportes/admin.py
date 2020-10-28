from django.contrib import admin
from django.utils.html import format_html
from reportes.models import *
from servicios.models import Servicio
from django.contrib.auth.models import User



class ReportAdmin(admin.ModelAdmin):
    search_fields = ['usuario']
    list_display = ['id', 'fecha', 'usuario', 'telefono', 'residencia', 'referencia', 'descripcion', 'Imagen', 'ubicacion', 'status', 'comprobante']
    list_filter = ['fecha', 'type', 'status']
    ordering = ['id'] #visualizaremos los datos ordenados por nombres

    def Imagen(self, obj):
        try:
            return format_html('<img src={} width="100" height="100"/>', obj.foto.url)
        except:
            pass

class TypesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['pk', 'name']
    list_filter = ['name']
    ordering = ['pk'] #visualizaremos los datos ordenados por nombres

    def Imagen(self, obj):
        try:
            return format_html('<img src={} width="100" height="75"/>', obj.foto.url)
        except:
            pass
#
# class AlumbradoPublicoAdmin(admin.ModelAdmin):
#     search_fields = ['usuario']
#     list_display = ['id', 'fecha', 'usuario', 'Imagen']
#     ordering = ['id'] #visualizaremos los datos ordenados por nombres
#
#     def Imagen(self, obj):
#         try:
#             return format_html('<img src={} width="100" height="75"/>', obj.foto.url)
#         except:
#             pass
#
# class CementerioAdmin(admin.ModelAdmin):
#     search_fields = ['usuario']
#     list_display = ['id', 'fecha', 'usuario', 'Imagen']
#     ordering = ['id'] #visualizaremos los datos ordenados por nombres
#
#     def Imagen(self, obj):
#         try:
#             return format_html('<img src={} width="100" height="75"/>', obj.foto.url)
#         except:
#             pass
#
# class MercadoAdmin(admin.ModelAdmin):
#     search_fields = ['usuario']
#     list_display = ['id', 'fecha', 'usuario', 'Imagen']
#     ordering = ['id'] #visualizaremos los datos ordenados por nombres
#
#     def Imagen(self, obj):
#         try:
#             return format_html('<img src={} width="100" height="75"/>', obj.foto.url)
#         except:
#             pass
#
# class TrenDeAseoAdmin(admin.ModelAdmin):
#     search_fields = ['usuario']
#     list_display = ['id', 'fecha', 'usuario', 'Imagen']
#     ordering = ['id'] #visualizaremos los datos ordenados por nombres
#
#     def Imagen(self, obj):
#         try:
#             return format_html('<img src={} width="100" height="75"/>', obj.foto.url)
#         except:
#             pass
#
# class TransportePublicoAdmin(admin.ModelAdmin):
#     search_fields = ['usuario']
#     list_display = ['id', 'fecha', 'usuario', 'Imagen']
#     ordering = ['id'] #visualizaremos los datos ordenados por nombres
#
#     def Imagen(self, obj):
#         try:
#             return format_html('<img src={} width="100" height="75"/>', obj.foto.url)
#         except:
#             pass
# # Register your models here.
#

admin.site.register(Report, ReportAdmin)
admin.site.register(TypeReport, TypesAdmin)
# admin.site.register(Reporte_AlumbradoPublico, AlumbradoPublicoAdmin)
# admin.site.register(Reporte_Cementerio, CementerioAdmin)
# admin.site.register(Reporte_Mercado, MercadoAdmin)
# admin.site.register(Reporte_TrendeAseo, TrenDeAseoAdmin)
# admin.site.register(Reporte_TransportePublico, TransportePublicoAdmin)
