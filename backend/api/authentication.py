from rest_framework.authentication import TokenAuthentication


class EcommerceTokenAuthentication(TokenAuthentication):
    # keyword = 'Token'  # default keyword
    keyword = 'Bearer'
