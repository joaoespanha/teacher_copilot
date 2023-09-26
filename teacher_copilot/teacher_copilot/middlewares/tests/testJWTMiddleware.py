from django.test import TestCase
from teacher_copilot.middlewares.JWTMiddleware import JWTMiddleware
from django.test.client import RequestFactory
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
import jwt


user_mock = {"username": "joaojoao", "password": "12345", "email": "jo@jo.com"}


class JWTMiddlewareTestCase(TestCase):
    def setUp(self):
        User = get_user_model()

        self.valid_user = User.objects.create(**user_mock)

        self.factory = RequestFactory()

        token_payload = {"user_id": self.valid_user.id}

        self.valid_token = jwt.encode(
            token_payload, settings.SECRET_KEY, algorithm="HS256"
        )
        self.invalid_token = "invalid token"

    def test_valid_token(self):
        request = self.factory.get("student:list")
        request.COOKIES["token"] = self.valid_token

        middleware = JWTMiddleware(get_response=lambda r: r)

        response = middleware(request)

        self.assertTrue(response.user.is_authenticated)

    def test_invalid_valid_token(self):
        request = self.factory.get("student:list")
        request.COOKIES["token"] = self.invalid_token

        middleware = JWTMiddleware(get_response=lambda r: r)

        middleware_session = SessionMiddleware(get_response=lambda r: r)
        request = middleware_session(request)

        response = middleware(request)

        self.assertEqual(response.url, "/auth/login")

    def test_inexistant_token(self):
        request = self.factory.get("student:list")

        middleware = JWTMiddleware(get_response=lambda r: r)

        middleware_session = SessionMiddleware(get_response=lambda r: r)
        request = middleware_session(request)

        response = middleware(request)

        self.assertEqual(response.url, "/auth/login")
