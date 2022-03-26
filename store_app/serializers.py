from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Adress,Customer,Product

class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Adress
        fields = ['id','street_and_number','postal_code','city','country']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id','name','category','quantity','size','price']


class CustomerSerializer(WritableNestedModelSerializer,
                            serializers.ModelSerializer):

    shipping_adress = AdressSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        
        model = Customer
        fields = ['id','first_name','last_name','email','credit_card','created_at','shipping_adress','products']
        depth = 1

    def create(self, validated_data):

        shipping_adress_data = validated_data.pop('shipping_adress')
        shipping_adress = AdressSerializer.create(AdressSerializer(), validated_data= shipping_adress_data)
        customer,created = Customer.objects.update_or_create(first_name = validated_data.pop('first_name'),last_name = validated_data.pop('last_name'),email = validated_data.pop('email'),
                              credit_card = validated_data.pop('credit_card') ,shipping_adress=shipping_adress)
        return customer