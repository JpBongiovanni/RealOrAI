from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_form, name="image_form"),
    path('metadata', views.image_metadata, name="image_metadata")
]