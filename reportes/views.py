from django.shortcuts import render, redirect
from django.urls import reverse , reverse_lazy
from django.views.generic import TemplateView , CreateView , DetailView, View
from django.contrib.messages.views import SuccessMessageMixin
from reportes.models import *
from reportes.views import *
from django.contrib import messages
from easy_pdf.views import PDFTemplateView
from django.contrib.auth.models import User
from servicios.models import Servicio 


# Create your views here.
from reportes.forms import *

"""Index view, use to welcome to page"""
class IndexView(TemplateView):
    template_name = 'reportes/index.html'

    """Add data to context """
    def get_context_data(self, *args , **kwargs):
        pass

class IndexView2(TemplateView):
    template_name = 'reportes/index2.html'

    """Add data to context """
    def get_context_data(self, *args , **kwargs):
        pass

"""Index view, use to welcome to page"""
class MapView(TemplateView):
    template_name = 'reportes/map.html'

    """Add data to context """
    def get_context_data(self, *args , **kwargs):
        pass
 
class CreateReport(SuccessMessageMixin, CreateView):
    template_name = 'reportes/create.html'

    form_class = ReportForm
    success_message = 'Se agrego el reporte correctamente'
    success_url = reverse_lazy('index2')

    """Agregar datos al contexto del formulario"""
    def get_context_data(self, **kwargs):
        ctx = super(CreateReport, self).get_context_data(**kwargs)
        ctx['types'] = TypeReport.objects.all()
        return ctx

class ReportList(TemplateView):
    template_name='reportes/list_report.html'

    def get_context_data(self, *args , **kwargs):
        reports = Report.objects.all().order_by('pk')
        return {'reports': reports}



class ViewInMap(DetailView):
    template_name = 'reportes/view_in_map.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Report.objects.all()
    context_object_name = 'report'

    def get_context_data(self , *args , **kwargs):
        context = super(ViewInMap, self).get_context_data(**kwargs)
        id_report = self.get_object()
        target = Report.objects.get(pk=id_report.pk)
        split = target.ubicacion.split(',')
        lat = split[0]
        lng = split[1]
        context['lat'] = lat
        context['lng'] = lng
        return context


class VoucherPDFView(PDFTemplateView):
    template_name = "comprobante.html"

    def get_context_data(self, **kwargs):
        ids = self.request.GET.get("id")
        report = Report.objects.get(id=ids)

        return super(VoucherPDFView, self).get_context_data(
            pagesize="Letter",
            title="comprobante",
            report=report,
            **kwargs
        )

class ImprimirPDFView(PDFTemplateView):
    #archivo donde se va a desplegar la info , hay una carpeta llamada templates
    template_name = "imprimir.html"

    def get_context_data(self, **kwargs):
        #se hace una instancia del objeto a iterar
        report = Report.objects.all()

        #parametros de salida del reporte,
        return super(ImprimirPDFView, self).get_context_data(
            pagesize="Letter landscape",
            title="imprimir",
            report=report,
            **kwargs
        )