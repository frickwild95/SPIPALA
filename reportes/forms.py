from django import forms
from reportes.models import Report
from servicios.models import Servicio
# from django.contrib.gis.geos import Point


class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = (
            'type',
            'usuario',
            'telefono',
            'residencia',
            'referencia',
            'descripcion',
            'foto',
            'ubicacion',

        )





# class ReporteForm(forms.ModelForm):
#
#     latitude = forms.DecimalField(
#         min_value=-90,
#         max_value=90,
#         required=True,
#     )
#     longitude = forms.DecimalField(
#         min_value=-180,
#         max_value=180,
#         required=True,
#     )
#
#     class Meta(object):
#         model = Reporte
#         exclude = []
#         widgets = {'point': forms.HiddenInput()}
#
#     def clean(self):
#         super().clean()
#         if any(x for x in ['latitude', 'longitude'] if x in self.changed_data):
#             latitude = float(self.cleaned_data['latitude'])
#             longitude = float(self.cleaned_data['longitude'])
#             self.cleaned_data['point'] = Point(longitude, latitude)
#
#     def __init__(self, *args, **kwargs):
#         try:
#             coordinates = kwargs['instance'].point.tuple    #If PointField exists
#             initial = kwargs.get('initial', {})
#             initial['longitude'] = coordinates[0]    #Set longitude from coordinates
#             initial['latitude'] = coordinates[1]    #Set Latitude from coordinates
#             kwargs['initial'] = initial
#         except (KeyError, AttributeError):
#             pass
#         super().__init__(*args, **kwargs)
