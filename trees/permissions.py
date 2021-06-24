from rest_framework import permissions

class IsSponsorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj,):
        if request.method == permissions.SAFE_METHODS:
            return True
        return request.user.is_sponsor

class IsCompanyOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj,):
        if request.method == permissions.SAFE_METHODS:
            return True
        return request.user.is_company
