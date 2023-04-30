from rest_framework import serializers


# Show user data in public
class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, user):
        products_related = user.product_set.all()[:5]
        # serializer_context = {
        #     'request': self.context.get('request')
        # }

        print('self.context: ', self.context)

        products_serializers = UserProductInlineSerializer(
            products_related,
            many=True, context=self.context
        )

        return products_serializers.data


class UserProductInlineSerializer(serializers.Serializer):

    # Model fields adding validators
    title = serializers.CharField(read_only=True)
    # end Model fields

    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
