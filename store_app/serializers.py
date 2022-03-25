from itertools import product
from pprint import pprint
from idna import valid_contextj
from rest_framework import serializers

from .models import Adress,Customer,Product

class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Adress
        fields = ['id','street_and_number','postal_code','city','country']




class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id','name','category','quantity','size','price']




class CustomerSerializer(serializers.ModelSerializer):
    shipping_adress = AdressSerializer()
    products = ProductSerializer(many=True,read_only = True)

    class Meta:


        model = Customer
        fields = ['id','first_name','last_name','email','credit_card','created_at','shipping_adress','products']
        depth = 1

        

    def create(self, validated_data):
        
        
        shipping_adress_data = validated_data.pop('shipping_adress')
        shipping_adress = AdressSerializer.create(AdressSerializer(), validated_data= shipping_adress_data)
        customer,created = Customer.objects.update_or_create(first_name = validated_data.pop('first_name'),last_name = validated_data.pop('last_name'),email = validated_data.pop('email'),
                              credit_card = validated_data.pop('credit_card'),products = validated_data.pop('products')  ,shipping_adress=shipping_adress)
        return customer
