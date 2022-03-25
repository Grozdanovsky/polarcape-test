from django.shortcuts import render
from .models import Adress,Customer,Product
from .serializers import AdressSerializer,CustomerSerializer,ProductSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class AdressViewSet(ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.select_related('shipping_adress').all()
    serializer_class = CustomerSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
