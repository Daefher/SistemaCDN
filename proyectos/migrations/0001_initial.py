# Generated by Django 2.0.2 on 2018-04-18 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('clienteID', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoP', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='progreso',
            fields=[
                ('idProgreso', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=128)),
                ('estado', models.BooleanField(default=False)),
                ('titulo', models.CharField(default=None, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('folio', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tomo', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('numero_instrumento', models.CharField(max_length=30)),
                ('enajenante', models.CharField(max_length=100)),
                ('adquirente', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=32)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('localizacion', models.CharField(default=None, max_length=20)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='progreso',
            name='id_proyecto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='escritura',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto'),
        ),
    ]