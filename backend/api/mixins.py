from rest_framework import permissions, authentication

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
