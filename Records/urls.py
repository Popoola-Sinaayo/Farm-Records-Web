from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('add-farmer', add_farmer_info, name="add-farmer"),
    path('tractor-info', tractor_info, name="tractor"),
    path('all-tractors', tractors),
    path('tractor/<int:id>', tractor_details, name="tractor-info")
]
