
from garden_app.models import Plant,PlantMeasurement
from garden_app.serializers import  PlantSerializer, PlantMeasurementSerializer, UserSerializer
# from garden_app.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from django.views.generic import ListView,DetailView
from django.views.generic import CreateView,UpdateView

class PlantListView(ListView):
    template_name = 'home.html'
    model = Plant
    context_object_name = 'all_plants_list'

class PlantDetailView(DetailView):
    template_name = 'plant.html'
    model = Plant
    context_object_name = 'plant'

class PlantCreateView(CreateView):
    template_name = 'plant_new.html'
    model = Plant
    fields = ['plant_species','image','plant_nickname','description','planted_date','retailer_name','water_needs','light_needs','temperature_needs']

class PlantUpdateView(UpdateView):
    template_name = 'plant_edit.html'
    model = Plant
    fields = ['plant_species','image','plant_nickname','description','retailer_name','water_needs','light_needs','temperature_needs']
















#API viewsets
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


#viewset for a single plant
class PlantViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

class PlantMeasurementViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = PlantMeasurement.objects.all()
    serializer_class = PlantMeasurementSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'plants': reverse('plant-list', request=request, format=format)
    })






