# Generated by Django 4.1.1 on 2022-09-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitores', '0002_remove_monitor_img_url_monitor_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=600)),
                ('edad_min', models.IntegerField()),
                ('edad_max', models.IntegerField()),
                ('monis', models.ManyToManyField(to='monitores.monitor')),
            ],
        ),
    ]
