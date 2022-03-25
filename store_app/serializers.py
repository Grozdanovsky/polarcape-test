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

    products = ProductSerializer(many=True,read_only = True)

    class Meta:


        model = Customer
        fields = ['id','first_name','last_name','email','credit_card','created_at','shipping_adress','products']