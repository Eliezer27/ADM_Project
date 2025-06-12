from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Componente, CaracteristicaDestacada

class CaracteristicaInline(admin.TabularInline):
    model = CaracteristicaDestacada
    extra = 1
    min_num = 0

@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion_corta', 'tiene_modelo_3d')
    search_fields = ('nombre', 'descripcion', 'especificaciones')
    # list_filter removido o corregido según necesidad
    inlines = [CaracteristicaInline]
    
    fields = (
        'nombre',
        'descripcion',
        'especificaciones',
        'detalles',
        'enlace_modelo_3d',
        'vista_previa_modelo',
    )
    readonly_fields = ('vista_previa_modelo',)

    def descripcion_corta(self, obj):
        return f"{obj.descripcion[:50]}..." if obj.descripcion else ""
    descripcion_corta.short_description = "Descripción corta"

    def tiene_modelo_3d(self, obj):
        return "✅" if obj.enlace_modelo_3d else "❌"
    tiene_modelo_3d.short_description = "3D"

    def vista_previa_modelo(self, obj):
        if embed := obj.modelo_3d_embed:
            return mark_safe(embed)
        return "No hay modelo 3D cargado o la URL no es válida"
    vista_previa_modelo.short_description = "Vista previa del modelo 3D"
    vista_previa_modelo.allow_tags = True

@admin.register(CaracteristicaDestacada)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'valor', 'componente')
    search_fields = ('nombre', 'valor', 'componente__nombre')