from django.urls import path, include
from rest_framework.routers import DefaultRouter
from garden_app import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'plant', views.PlantViewSet)
router.register(r'plant_measurement', views.PlantMeasurementViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.PlantListView.as_view(),name='home'),
    path('plant/new/', views.PlantCreateView.as_view(),name='plant_new'),
    path('plant/<int:pk>', views.PlantDetailView.as_view(),name='plant_detail'),
    path('plant/<int:pk>/edit', views.PlantUpdateView.as_view(),name='plant_edit'),
    path('api/', include(router.urls)),
]