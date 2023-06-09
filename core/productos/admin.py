from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    

    list_display = ['titulo', 'precio', 'detalle', 'capacidad', 'imagen']
    list_filter = ['titulo', 'capacidad']
    
    
    # Register your models here.
admin.site.register(Producto, ProductoAdmin)
