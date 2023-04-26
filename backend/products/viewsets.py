from rest_framework import viewsets, authentication

from api.mixins import AuthenticationMixin, StaffEditorPermissionMixin
from api.authentication import EcommerceTokenAuthentication
from .models import Product
from .serializers import ProductSerializer


# class ProductViewSet(
#     AuthenticationMixin,
#     StaffEditorPermissionMixin,
#     viewsets.ModelViewSet
# ):
#     """
#     Using viewsets.ModelViewSet
#     GET -> list -> queryset
#     GET -> retrieve -> Product instance (Detail View)
#     POST -> create -> create a new Product instance
#     PUT -> update -> update a Product instance
#     PATCH -> update -> partial update a Product instance
#     DELETE -> delete -> destroy a Product instance
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_fields = 'pk'  # default


class ProductViewSetListCreateAPIView(
    AuthenticationMixin,
    StaffEditorPermissionMixin,
    viewsets.ReadOnlyModelViewSet
):
    '''
    Using viewsets.generics.ListCreateAPIView \n
    GET -> list -> queryset \n
    GET -> retrieve -> Product instance (Detail View) \n
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [StaffEditorPermissionMixin]
    lookup_fields = 'pk'  # default

# product_list_view = ProductViewSetListCreateAPIView.as_view({'get': 'list'})
# product_detail_view = ProductViewSetListCreateAPIView.as_view({'get': 'retrieve'})
