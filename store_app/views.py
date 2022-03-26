import re
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.filters import  OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AdressSerializer, CustomerProductsSerializer,CustomerSerializer,ProductSerializer
from .models import Adress,Customer,Product
from .filters import ProductFilter
from .response import response_message

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

        if credit_card.isdigit() and credit_card.startswith('4' or '5' or '6') and not re.search(r'(.)\1\1\1', credit_card):

            customer = get_object_or_404(Customer.objects.select_related('shipping_adress').all(), pk=pk)
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



class AddProductToCusomer(APIView):

    def post(self,request):
        try:
            product_id = request.data['products']
            product = Product.objects.all().get(id = product_id)
            product.quantity -= 1
            product.save()

            serializer = CustomerProductsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(response_message(f"Product {product.name} added."))
        except ObjectDoesNotExist:
            return Response(response_message("Product does not exist"))


@api_view(["GET","DELETE"])
def delete_product_from_user(request,customer_id):
    
    if request.method == "DELETE":
        try:
            customer = Customer.objects.get(pk = customer_id)

            product = Product.objects.get(pk = request.data['product_id']) 
            product_id = request.data['product_id']
            product = Product.objects.all().get(id = product_id)
            product.quantity += 1
            product.save()
            customer.products.remove(product)
            

            return Response(response_message(f"Product {product.name} deleted"))
        except :
            return Response(response_message(f"Product not found"))