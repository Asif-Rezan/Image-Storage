from .serializers import ImageSerializer
from .models import Images
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Images
# Create your views here.


@api_view(['GET'])
def ImageApi(request):

  images= Images.objects.all()

  serializer=ImageSerializer(images,many=True)

  return Response(serializer.data)

