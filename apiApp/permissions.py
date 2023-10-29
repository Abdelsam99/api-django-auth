from rest_framework import permissions

class IsStaffPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)
    """Ici c'est pour avoir le contrôle total sur des permission"""
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    """C'est notre logique de permission qu'on a ecrit ici"""
    # def has_permission(self, request, view):
    #     user=request.user
    #     if user.is_staff:
    #         if user.has_perm('apiApp.add_Product'): #app_name.perm_nam_model_name(add, delete, view, change)
    #             return True
    #         if user.has_perm('apiApp.change_Product'): #app_name.perm_nam_model_name(add, delete, view, change)
    #             return True
    #         if user.has_perm('apiApp.delete_Product'): #app_name.perm_nam_model_name(add, delete, view, change)
    #             return True
    #         if user.has_perm('apiApp.view_Product'): #app_name.perm_nam_model_name(add, delete, view, change)
    #             return True
    #         return True
    #     return False
class IsAuthenticatedOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)