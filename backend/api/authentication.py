# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# class EcommerceTokenAuthentication(TokenAuthentication):
#     # keyword = 'Token'  # default keyword
#     keyword = 'Bearer'


class EcommerceTokenAuthentication(JWTAuthentication):
    # keyword = 'Token' # default keyword
    keyword = 'Bearer'
    # keyword = 'JWT'
