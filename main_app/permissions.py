from rest_framework import permissions

def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'admin'

class IsAdminUserOrReadOnly(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return is_admin(request.user)
