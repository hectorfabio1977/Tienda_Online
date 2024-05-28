# Generated by Django 5.0.6 on 2024-05-28 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Codigo_Departamento", models.CharField(max_length=10)),
                ("Nombre", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Departamentos",
                "db_table": "Departamentos",
                "ordering": ["Nombre"],
            },
        ),
        migrations.CreateModel(
            name="Ciudad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Codigo_Ciudad", models.TextField(max_length=10)),
                ("Nombre", models.CharField(max_length=100)),
                (
                    "Departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Proveedores.departamento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ciudad",
                "verbose_name_plural": "Ciudades",
                "db_table": "Ciudades",
                "ordering": ["Nombre"],
            },
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("contacto", models.CharField(max_length=50)),
                ("direccion", models.CharField(max_length=255)),
                ("pais", models.CharField(max_length=100)),
                ("sitio_web", models.URLField(blank=True, max_length=100, null=True)),
                ("productos_suministrados", models.TextField()),
                ("fecha_registro", models.DateField()),
                ("ultima_actualizacion", models.DateTimeField(auto_now=True)),
                (
                    "ciudad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Proveedores.ciudad",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proveedor",
                "verbose_name_plural": "Proveedores",
                "db_table": "Proveedores_2",
                "ordering": ["nombre"],
            },
        ),
    ]
