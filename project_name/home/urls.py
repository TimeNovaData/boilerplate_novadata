from django.urls import path
from .views import home, design_system,svg_viewer



urlpatterns = [
    path('', home, name='home'),
    path('design_system/', design_system, name='design_system'),
    path('svg_viewer/', svg_viewer, name='svg_viewer'),
]
