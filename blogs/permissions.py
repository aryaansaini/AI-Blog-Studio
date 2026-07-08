from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS sabke liye allow
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Sirf author hi update/delete kar sakta hai
        return obj.author == request.user