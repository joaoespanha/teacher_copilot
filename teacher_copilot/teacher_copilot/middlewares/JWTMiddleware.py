import jwt
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User


class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Define a list of paths where the middleware should be skipped
        self.paths_to_skip = ["/auth/login", "/auth/logout"]

    def should_skip_middleware(self, request):
        # Get the current path from the request
        current_path = request.path_info

        # Check if the current path is in the list of paths to skip
        return current_path in self.paths_to_skip

    def __call__(self, request):
        if self.should_skip_middleware(request):
            return self.get_response(request)

        try:
            token = request.COOKIES["token"]
        except KeyError:
            logout(request)
            return redirect("authorization:login")

        if not token:
            logout(request)
            return redirect("authorization:login")
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

            user_id = decoded_token["user_id"]

            user = User.objects.get(id=user_id)

            request.user = user

        except jwt.ExpiredSignatureError:
            logout(request)
            return redirect("authorization:login")
        except jwt.InvalidTokenError:
            logout(request)
            return redirect("authorization:login")

        response = self.get_response(request)

        return response
