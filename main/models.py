from django.db import models
from django.utils.safestring import mark_safe
class Componente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    especificaciones = models.TextField(help_text="Puedes usar formato JSON o texto plano.")
    detalles = models.TextField(blank=True, null=True)

    enlace_modelo_3d = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL del modelo 3D de Sketchfab (ej: https://sketchfab.com/models/ID-MODELO)"
    )

    def __str__(self):
        return self.nombre

    @property
    def modelo_3d_embed(self):
        if not self.enlace_modelo_3d:
            return None
            
        # Extrae el ID del modelo de la URL
        if "sketchfab.com/models/" in self.enlace_modelo_3d:
            modelo_id = self.enlace_modelo_3d.split("sketchfab.com/models/")[1].split("/")[0]
        else:
            return None
            
        # Validación básica del ID
        if not modelo_id.isalnum() or len(modelo_id) != 32:  # Los IDs de Sketchfab tienen 32 caracteres
            return None
            
        return mark_safe(f"""
        <iframe 
            title="{self.nombre}" 
            frameborder="0" 
            allowfullscreen 
            mozallowfullscreen="true" 
            webkitallowfullscreen="true" 
            allow="autoplay; fullscreen; xr-spatial-tracking" 
            xr-spatial-tracking 
            execution-while-out-of-viewport 
            execution-while-not-rendered 
            web-share 
            src="https://sketchfab.com/models/{modelo_id}/embed">
        </iframe>
        """)

class CaracteristicaDestacada(models.Model):
    componente = models.ForeignKey(
        Componente, 
        on_delete=models.CASCADE, 
        related_name='caracteristicas'  # Este es el related_name importante
    )
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"