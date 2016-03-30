from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    BASICAUTH_USERS={"username": "password"}
)
class TestBasicAuthDecorator(TestCase):

    def test__it(self):
        res = self.client.get("/decorated/", HTTP_AUTHORIZATION="Basic dXNlcm5hbWU6cGFzc3dvcmQ=")
        self.assertEqual(res.content, b"Called")

    def test__hasnt_authorization_header(self):
        res = self.client.get("/decorated/")
        self.assertEqual(res.status_code, 401)

    def test__invalid_user(self):
        res = self.client.get("/decorated/", HTTP_AUTHORIZATION="Basic aW52YWxpZDppbnZhbGlk")
        self.assertEqual(res.status_code, 401)
