from django.urls import path
from . import api

urlpatterns = [
    path('', api.properties_list, name='properties_list'),  # Ruta para obtener todas las propiedades
    path('create/', api.create_property, name='api_create_property'),
    path('<uuid:pk>/', api.properties_detail, name='api_properties_detail'),
    
]
