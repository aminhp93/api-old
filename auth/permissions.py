from django.contrib.auth.models import User
from rest_framework import permissions

class TestPermission(permissions.BasePermission):
    message = 'This action is only reserved for platform developer.'

    def has_permission(self, request, view):
        print(request.user)
        return True
