from django.contrib.auth import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Images

class ImageSerializer(ModelSerializer):
  class Meta:
    model= Images
    fields='__all__'