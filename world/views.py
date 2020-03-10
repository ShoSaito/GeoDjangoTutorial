from django.shortcuts import render
from django.views.generic import TemplateView
from .models import WorldBorder

from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import generics,viewsets
from . import serializers
from rest_framework.pagination import PageNumberPagination


from django.core.serializers import serialize
from django.http import HttpResponse
# Create your views here.

class MapView(TemplateView):
    template_name="world/index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["WorldBorder"] = WorldBorder.objects.get(name="Taiwan") 
        return context

class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.filter(name="Taiwan")
    serializer_class = serializers.WorldBorderSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

def api_get_worldborder(request):
    # utm_poly = serialize('geojson', WorldBorder.objects.filter(name="Taiwan"), geometry_field='mpoly', fields=('zone', 'zone_hemi'))
    # worldborder = serialize('geojson', WorldBorder.objects.filter(name="Taiwan"), geometry_field='mpoly')
    worldborder = serialize('geojson', WorldBorder.objects.all(), geometry_field='mpoly')
    return HttpResponse(worldborder, content_type='application/json')
        
