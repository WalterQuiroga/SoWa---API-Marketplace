from django.urls import path
from .views import ProductoView


urlpatterns = [
    
    
    
    path('', ProductoView.as_view(), name='producto'),
    path('<int:pk>', ProductoView.as_view(), name='un_producto'),
        
    ]