from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        print('description: ', description)
        if description is None:
            description = title
            serializer.save(description=description)
        return super().perform_create(serializer)


product_list_create_view = ProductListCreateView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # ProductDetailAPIView means getting only single Product
    # lookup_field= 'pk'


product_detail_view = ProductDetailAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # ProductListAPIView means getting  list of Products


# product_list_view = ProductListAPIView.as_view()
