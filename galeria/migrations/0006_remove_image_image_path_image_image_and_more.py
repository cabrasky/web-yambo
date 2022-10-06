# Generated by Django 4.1.1 on 2022-10-03 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0005_remove_image_route_image_image_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_path',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.FileField(null=True, upload_to='galeria/'),
        ),
        migrations.AddField(
            model_name='image',
            name='imageuploader_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]