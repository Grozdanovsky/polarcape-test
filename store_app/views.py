from pprint import pprint
import re
from django.db import IntegrityError
from django.forms import IntegerField
from django.shortcuts import get_object_or_404
from django.db.models import TextField
from django.db.models.functions import Cast
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.filters import  OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import AdressSerializer,CustomerSerializer,ProductSerializer
from .models import Adress,Customer,Product
from .filters import ProductFilter

# Create your views here.


class AdressViewSet(ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer

class CusomerList(APIView):
    
    def get(self,request):
        queryset = Customer.objects.select_related('shipping_adress').prefetch_related('products').all()
        serializer = CustomerSerializer(queryset,many = True)

        return Response(serializer.data)


    def post(self,request):
            credit_card = request.data['credit_card']
            if credit_card.isdigit() and credit_card.startswith('4' or '5' or '6') and not re.search(r'(.)\1\1\1', credit_card):
                try:
                    for product_id in request.data['products']:
                        product = Product.objects.all().get(id = product_id)
                        product.quantity -= 1
                        product.save()
                
                except IntegrityError:
                    return Response({'error': 'This product is no longer available we are sorry.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                serializer = CustomerSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response(serializer.data,status=status.HTTP_201_CREATED)

            else:
                return Response({'error' : "Invalid Credit card input"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CustomerDetail(APIView):

    def get(self,request,pk):
        customer = get_object_or_404(Customer.objects.select_related('shipping_adress').all(), pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self,request,pk):
        credit_card = request.data['credit_card']
        old_products_str = list(Customer.objects.filter(pk=pk).annotate(str_id=Cast('products', output_field=TextField())).values_list('str_id', flat=True))
        old_products = []
        if old_products_str != [None]:
            old_products = [int(number) for number in old_products_str]



        if credit_card.isdigit() and credit_card.startswith('4' or '5' or '6') and not re.search(r'(.)\1\1\1', credit_card):

            customer = get_object_or_404(Customer.objects.select_related('shipping_adress').prefetch_related('products').all(), pk=pk)

            try:

                for product_id in request.data['products']:
                    if product_id not in old_products or old_products == []:
                        product = Product.objects.all().get(id = product_id)
                        product.quantity -= 1
                        product.save()
                
            except IntegrityError:

                return Response({'error': 'This product is no longer available we are sorry.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                
            serializer = CustomerSerializer(customer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data,status=status.HTTP_200_OK)

        else:
            return Response({'error' : "Invalid Credit card input"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

    def delete(self,request,pk):

        customer = get_object_or_404(Customer.objects.select_related('shipping_adress').all(),pk=pk)
        customer.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price']