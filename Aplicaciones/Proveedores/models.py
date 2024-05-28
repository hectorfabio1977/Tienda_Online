from django.db import models

# Create your models here.
class Departamento(models.Model):
    Codigo_Departamento = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['Nombre']  # Ordena los departamentos por nombre
        db_table = 'Departamentos'  # Nombre de la tabla en la base de datos
        app_label = 'Proveedores'

class Ciudad(models.Model):
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Codigo_Ciudad = models.TextField(max_length=10)
    Nombre = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['Nombre']  # Ordena las ciudades por nombre
        db_table = 'Ciudades'  # Nombre de la tabla en la base de datos
        app_label = 'Proveedores'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100)
    sitio_web = models.URLField(max_length=100, blank=True, null=True)
    productos_suministrados = models.TextField()
    fecha_registro = models.DateField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']  # Ordena los proveedores por nombre
        db_table = 'Proveedores_2'  # Nombre de la tabla en la base de datos
        app_label = 'Proveedores'

