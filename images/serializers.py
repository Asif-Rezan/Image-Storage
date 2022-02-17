from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Category, Images

class ImageSerializer(ModelSerializer):
  class Meta:
    model= Images
    fields='__all__'


class CategorySerializer(ModelSerializer):
  class Meta:
    model=Category
    fields='__all__'