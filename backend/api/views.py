import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
# Create your views here.


# using '@api_view' decorator
@api_view(['GET'])
def api_home(request, *arg, **kwargs):
    """
    Django REST Framework API
    GET /products
    """
    print('api home')
    # data = request.data if request.data else {}
    # return Response(data)
    if instance := Product.objects.all().order_by('?').first():
        # must be add 'serializer_context' to ProductSerializer
        # for serializers.HyperlinkedIdentityField
        serializer_context = {
            'request': request,
        }

        data = ProductSerializer(
            instance=instance, context=serializer_context).data
    else:
        data = {}
    return Response(data)


@api_view(['POST'])
def add_products(request, *arg, **kwargs):
    """
    Django REST Framework API
    POST /products
    """
    serializer_context = {
        'request': request,
    }
    serializer = ProductSerializer(
        data=request.data, context=serializer_context)
    data = serializer.data if serializer.is_valid(raise_exception=True) else {}
    return Response(data)


# *************************************
# def api_home(request, *arg, **kwargs):

#     data = {}
#     body = request.body  # byte string of JSON data
#     try:
#         # convert byte string of JSON data(body) into Python Dict
#         data = json.loads(body)
#     except Exception as e:
#         raise e

#     print("Data: ", data)
#     # print("Request: ", body.decode("utf-8"))
#     # print("Request: ", dir(request))
#     print('request.headers: ', dict(request.headers))
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
