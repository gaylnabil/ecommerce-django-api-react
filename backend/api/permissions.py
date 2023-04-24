from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # override 'perms_map' in the class DjangoModelPermissions
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # # using overrides 'has_permission' with overrides 'perms_map' in the class DjangoModelPermissions
    # def has_permission(self, request, view):
    #     user = request.user
    #     print("user permissions: ", user.get_all_permissions())
    #     return super().has_permission(request, view) if user.is_staff else False

    # def has_permission(self, request, view):
    #     user = request.user
    #     print("user permissions: ", user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #         return bool(user.has_perm("products.delete_product"))
    #     return False

    # def has_object_permissions(self, request, view, obj):

    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True

    #     # Instance must have an attribute named `owner`.
    #     return obj.owner == request.user

    # # end def
