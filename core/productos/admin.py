from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'precio', 'detalle']
    list_filter = ['titulo']
    
    
    # Register your models here.
admin.site.register(Producto, ProductoAdmin)
