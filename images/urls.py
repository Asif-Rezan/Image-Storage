from . import views
from django.urls import path

urlpatterns = [
    path('images/',views.ImageApi,name='img-api'),
    path('category/',views.ImageCategory),
]
