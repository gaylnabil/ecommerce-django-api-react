from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from .validators import validate_title, unique_product_title


class ProductSerializer(serializers.ModelSerializer):
    """
    A serializer class that serializes instances of the `Product` model.

    This serializer includes fields such as `pk`, `title`, `description`,
    `price`, and more. It also includes custom fields such as `my_discount`
    and `url`. The former is calculated using the instance method
    `get_discount()` on the object if it exists, while the latter returns
    a URL string based on the primary key of the object.

    Attributes:
        my_discount (serializers.SerializerMethodField): A custom field that
            calculates and returns a discount value for each product.
        url (serializers.SerializerMethodField): A custom field that returns
            a URL string based on each product's primary key.

    Methods:
        get_url(obj): Returns a URL string based on an object's primary key.
        get_my_discount(obj): Calculates and returns a discount value for an
            object if it has an id attribute and is an instance of Product.

    Meta:
        model: The Django model to serialize (`Product`).
        fields: The list of fields to include in serialization output,
            including both built-in fields like 'pk' and custom ones like
            'my_discount' or 'url'.

    Usage Example:

    ```
    # Create an instance of this serializer with some data

    serialized_data = ProductSerializer(data={
        "title": "My Awesome Product",
        "description": "This is my awesome product.",
        "price": 100.0,
        "sale_price": 80.0,
        ...
    })

    # Check if data is valid before saving

    if serialized_data.is_valid():

        # Save validated data to database or use elsewhere

        saved_product = serialized_data.save()
    ```
    """

    # Model fields
    title = serializers.CharField(validators=[unique_product_title])
    # end Model fields
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    edit_url = serializers.SerializerMethodField(read_only=True)

    email = serializers.EmailField(write_only=True)

    def create(self, validated_data):
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        print('validated_data Created: ', obj, '; Email: ', email)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        print('ProductSerializer: validated_data Updated: ',
              instance, '; Email: ', email)
        # if instance.description is None:
        #     instance.description = instance.title
        #     instance.save()
        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None

        return reverse('product-update', kwargs={'pk': obj.pk}, request=request)

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
            'category',
            'url',
            'edit_url',
            'email',
            # 'user'
        ]
