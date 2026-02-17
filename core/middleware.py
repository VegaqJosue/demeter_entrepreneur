from .current_user import set_current_user

class CurrentUserMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        set_current_user(getattr(request, "user", None))
        response = self.get_response(request)
        return response

class TenantMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        request.tenant = None

        user = getattr(request, "user", None)

        if user and user.is_authenticated:
            if user.user_scope == "TENANT":
                request.tenant = user.tenant
            elif user.user_scope == "PLATFORM":
                request.tenant = None
        
        response = self.get_response(request)
        return response