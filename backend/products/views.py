from rest_framework import generics, mixins, authentication
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import Http4
from django.shortcuts import get_object_or_404

# Costume Staff Permissions
from api.mixins import StaffEditorPermissionMixin
from api.authentication import EcommerceTokenAuthentication
from .models import Product


# Using generics API View.
class ProductListCreateView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView,
):
    """
    A view that provides both list and create functionality for Products.

    """
    queryset = Product.objects.all()
    # The serializer class to use for Product objects.
    serializer_class = ProductSerializer
    #  used by this view. In this case, it uses SessionAuthentication which requires
    #  clients to authenticate using Django sessions.
    authentication_classes = [
        authentication.SessionAuthentication, EcommerceTokenAuthentication]

    def perform_create(self, serializer):
        """
        Overrides the default behavior when creating a new object via POST request. 
        It sets the description field of newly created product equal to its title 
        if no description is provided.

        """
        print("perform_create: ", serializer.validated_data)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        print('description: ', description)
        if description is None:
            description = title

        serializer.save(description=description)
        return super().perform_create(serializer)


product_list_create_view = ProductListCreateView.as_view()


class ProductDetailAPIView(
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin
):
    """
    A view that retrieves a single product instance by its ID.

    **Attributes:**

    - `queryset`: The queryset of all products.

    - `serializer_class`: The serializer class used to serialize/deserialize the data.

    **Methods:**

     - `retrieve(self, request, *args, **kwargs)`: Retrieves and returns a single product instance by its ID.

     """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    # ProductDetailAPIView means getting only single Product
    # lookup_field= 'pk'
product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    generics.UpdateAPIView,
    StaffEditorPermissionMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # ProductDetailAPIView means getting only single Product
    lookup_field = 'pk'

    authentication_classes = [authentication.SessionAuthentication]

    def perform_update(self, serializer):
        print("perform_update: ", serializer.validated_data)
        instance = serializer.save()
        if instance.description is None:
            instance.description = instance.title
            instance.save()
        return super().perform_update(instance)


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    generics.DestroyAPIView,
    StaffEditorPermissionMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # ProductDetailAPIView means getting only single Product
    lookup_field = 'pk'

    authentication_classes = [
        authentication.SessionAuthentication,
        EcommerceTokenAuthentication
    ]

    def perform_destroy(self, instance):
        print("perform_destroy: ", instance)
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # ProductListAPIView means getting  list of Products


# product_list_view = ProductListAPIView.as_view()

# using @api_view
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method  # GET, POST, PUT, DELETE

    if method == 'GET':
        if pk is not None:
            # Detail View
            # queryset = Product.objects.filter(pk=pk).first()
            # serializer = ProductSerializer(queryset)
            obj = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(obj)
        else:
            # List Views
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    elif method == 'POST':
        """
        Django REST Framework API
        POST /products
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description') or None
            print('description: ', description)
            if description is None:
                description = title
                serializer.save(description=description)
            data = serializer.data
        return Response(data)


# Using Mixin and Generics API View
class ProductMixinView(
        mixins.CreateModelMixin,  # Create a new Product
        mixins.ListModelMixin,  # List of products
        mixins.RetrieveModelMixin,  # getting details of a product
        mixins.UpdateModelMixin,  # updating a product
        mixins.DestroyModelMixin,  # Delete a product
        generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # POST /products

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("ProductMixinView: perform_create => ", serializer.validated_data)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        print('description: ', description)
        if description is None:
            description = title

        serializer.save(description=description)
        return super().perform_create(serializer)
    # ********************************************************
    # GET /products

    def get(self, request, *args, **kwargs):
        print('GET /products: ', args, '==>', kwargs)
        # 'self.list()' has token from 'mixins.ListModelMixin'
        pk = kwargs.get('pk')
        if pk is not None:
            # Detail View
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # PUT /products/:pk
    def put(self, request, *args, **kwargs):
        print('PUT /products/:pk/: ', args, '==>', kwargs)
        # 'self.list()' has token from 'mixins.ListModelMixin'
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        print("ProductMixinView: perform_update => ", serializer.validated_data)
        instance = serializer.save()
        if instance.description is None:
            instance.description = instance.title
            instance.save()
        return super().perform_update(instance)

    # DELETE /products/:pk
    def delete(self, request, *args, **kwargs):
        print('DELETE /products/:pk/: ', args, '==>', kwargs)
        # 'self.list()' has token from 'mixins.ListModelMixin'
        return self.destroy(request, *args, **kwargs)


product_mixin_view = ProductMixinView.as_view()
