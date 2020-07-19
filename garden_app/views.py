from django.shortcuts import render


from garden_app.models import Plant,PlantMeasurement,ArduinoPin
from garden_app.serializers import  PlantSerializer, PlantMeasurementSerializer, UserSerializer,ArduinoPinSerializer
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
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class PlantListView(ListView):
    template_name = 'plant_list.html'
    model = Plant
    context_object_name = 'plants'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PlantListView, self).get_context_data(**kwargs)
        return context



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

class ArduinoPinViewSet(viewsets.ModelViewSet):

    serializer_class = ArduinoPinSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = ArduinoPin.objects.all()
        arduino_id_param = self.request.query_params.get('arduino_id', None)
        is_collecting_param = self.request.query_params.get('is_collecting', None)
        if arduino_id_param is not None:
            queryset = queryset.filter(arduino_id=arduino_id_param)
            queryset = queryset.filter(is_collecting=is_collecting_param)
        return queryset


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'plants': reverse('plant-list', request=request, format=format),
        'arduino_pin': reverse('arduino_pin-list', request=request, format=format),
    })





from django.shortcuts import render
from django.db.models import Sum,Avg, Min,Max
from django.http import JsonResponse



def barchart(request):
    return render(request, 'barchart.html')


def measurement_chart(request):
    labels = []
    data = []

    queryset = PlantMeasurement.objects.values('plant_id','environmental_dimension').annotate(value_population=Avg('environmental_value')).order_by('-plant_id')
    for entry in queryset:
        labels.append(entry['environmental_dimension'])
        data.append(entry['value_population'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })