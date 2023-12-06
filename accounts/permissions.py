
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Foydalanuvchi faqat o'z profili uchun ruxsat beradi
        return obj.user == request.user
