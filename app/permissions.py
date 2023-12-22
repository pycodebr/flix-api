from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    """
    Global model permissions
    """

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(request.method, view)

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_suffix(method)
            return f"{app_label}.{action}_{model_name}"
        except AttributeError:
            return None

    def __get_action_suffix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
