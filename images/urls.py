from . import views
from django.urls import path

urlpatterns = [
    path('images/',views.ImageApi),
    path('category/',views.ImageCategory),
]
