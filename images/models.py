from django.db import models

# Create your models here.




class Images(models.Model):
  title=models.CharField(max_length=200,null=True)
  image=models.ImageField(upload_to='images/', blank=True)


  def __str__(self) -> str:
      return self.title

