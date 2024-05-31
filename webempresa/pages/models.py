from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Page(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = HTMLField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")


    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order', 'title']
    
    def __str__(self) -> str:
        return self.title