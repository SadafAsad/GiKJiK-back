from rest_framework import permissions
from django.shortcuts import get_object_or_404
from GiKJiK.models import *

class IsClassOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        t_class = get_object_or_404(Class, class_id=view.kwargs.get('class_id'))
        user = request.user
        if t_class.owner == user.user_profile:
            return True
        return False
