from rest_framework import serializers

from .models import Adress,Customer,Product

class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Adress
        fields = ['id','street_and_number','postal_code','city','country']


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = ['id','first_name','last_name','email','credit_card','created_at','shipping_adress']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id','name','category','quantity','size','price']
