# Generated by Django 4.0 on 2022-02-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_category_alter_images_image_images_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnail/'),
        ),
    ]
