from django_framework import serializers
from store.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end')

    def to_representation(self, instance):
        date = super().to_representation(instance)
