from rest_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_on_sale'] = instance.is_on_sale()
        date['current_price'] = instance.current_price()
        return data


from store.models import Product
product = Product.object.all()[0]
product = Product.objects.all()[0]
from store.serializers import ProductSerializer
