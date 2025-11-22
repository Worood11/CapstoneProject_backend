from rest_framework import permissions
from rest_framework.permissions import BasePermission

def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'admin'

class IsAdminUserOrReadOnly(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return is_admin(request.user)



class IsReviewOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
          return obj.user == request.user or is_admin(request.user)