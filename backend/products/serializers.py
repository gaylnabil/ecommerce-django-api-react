from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id') or not isinstance(obj, Product):
            return None
        return obj.get_discount()

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'description',
            'price',
            'sale_price',
            'my_discount',
            'category'
        ]
