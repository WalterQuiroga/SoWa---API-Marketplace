from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from .serializers import ProductoSerializer

from .models import Producto



# Create your views here.
def index_producto(request):
    return JsonResponse({"message": "Online"})

class ProductoView(APIView):
    def get(self, request, pk = None):
        if pk:
            producto = get_object_or_404(Producto, pk=pk)
            serializer = ProductoSerializer(producto)

        else:
            productos = Producto.objects.all()
            serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print(request.data)
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)