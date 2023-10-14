from rest_framework.permissions import BasePermission


class ViewSetPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated():
            if view.action == 'create' and not request.is_staff:
                return True
            elif view.action == 'delete':
                return request.user == view.get_object().user
            elif view.action in ['list', 'retrieve', 'update', 'partial_update', ] and request.user == view.get_object(
                                ).user or request.user == request.user.is_staff:
                return True
            else:
                return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().user


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True


