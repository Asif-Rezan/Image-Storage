from django.db import models
from PIL import Image
# Create your models here.
from django_resized import ResizedImageField


class Category(models.Model):
  name=models.CharField(max_length=100)

  def __str__(self) -> str:
      return self.name





class Images(models.Model):
  title=models.CharField(max_length=200,null=True)
  image=models.ImageField(upload_to='images/', blank=True)
  image_thumbnail=ResizedImageField(quality=5, upload_to='thumbnail/',blank=True)
  category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)


  #models.ImageField(upload_to='thumbnail/', blank=True)

  def __str__(self) -> str:
      return self.title

