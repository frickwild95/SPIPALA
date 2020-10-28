from django.contrib import admin
from servicios.models import Servicio
#from servicios.forms import ServicioForm

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    #form = ServicioForm
    list_display = ['id','nombre']

# admin.site.register(Servicio, ServicioAdmin)
