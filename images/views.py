from .serializers import CategorySerializer, ImageSerializer
from .models import Category, Images
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from .models import Images
# Create your views here.


class ImageApiPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3
    





class ImageApi(ListAPIView):

  queryset= Images.objects.all()

  serializer_class=ImageSerializer
 
  pagination_class =ImageApiPagination
 

@api_view(['GET'])
def ImageCategory(request):
  category=Category.objects.all()

  serializer=CategorySerializer(category,many=True)

  return Response(serializer.data)

