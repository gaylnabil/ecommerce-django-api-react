from rest_framework import permissions, authentication
from products.models import Product
from api.authentication import EcommerceTokenAuthentication
from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():

    permission_classes = [
        IsStaffEditorPermission,
        permissions.IsAdminUser
    ]


class AuthenticationMixin(object):

    #  used by this view. In this case, it uses SessionAuthentication which requires
    #  clients to authenticate using Django sessions.
    authentication_classes = [
        authentication.SessionAuthentication,
        EcommerceTokenAuthentication
    ]


class UserQuerySetMixin():
    """
    A mixin class that filters querysets based on the user field.

    Attributes:
        user_field (str): The name of the user field to filter by. 
        Default is 'user'.
    """
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        """
        Returns a filtered queryset based on the current request's authenticated user.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            QuerySet: A filtered queryset based on the current request's authenticated user.
            If no authenticated user exists, an empty queryset is returned.
        """
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()

        qs = super().get_queryset(*args, **kwargs)
        print('QS: ', qs)

        if user.is_superuser:
            return qs

        lookup_data = {self.user_field: user}

        print('lookup_data: ', lookup_data)

        return qs.filter(**lookup_data)
