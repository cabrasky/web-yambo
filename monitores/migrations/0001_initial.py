# Generated by Django 4.1.1 on 2022-09-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=600)),
                ('img_url', models.URLField(max_length=60)),
            ],
        ),
    ]
