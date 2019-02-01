from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from rest_framework.test import APIClient, APIRequestFactory
from tokenauth.api_settings import api_settings

from picontrol.control import write_pin_mode, write_pin_value
from pins.views import PinView

# Create your tests here.

class PinApiTest(TestCase):
    PIN = 11
    TEST_USERNAME = "test_user"
    TEST_PASSWORD = "test_password"
    OUT_MODE = 0
    IN_MODE = 1
    HIGH_VALUE = 1
    LOW_VALUE = 0

    def setUp(self):
        User = get_user_model()

        self.test_user = User.objects.create(username=self.TEST_USERNAME, is_active=True)
        self.test_user.set_password(self.TEST_PASSWORD)
        self.test_user.save()


        self.factory = APIRequestFactory()

        self.api_client = APIClient()
        response = self.api_client.post("/tokens/",
                                        {"username": self.TEST_USERNAME, "password": self.TEST_PASSWORD},
                                        format="json")

        self.assertEqual(response.status_code, 200)
        self.token = response.data.get('token')
        self.api_client.credentials(HTTP_AUTHORIZATION=api_settings.TOKEN_PREFIX + " " + self.token)

    def test_get_pin_permission(self):
        url = "/pins/api/%s" % self.PIN
        request = self.factory.get(url)
        request.user = AnonymousUser()

        response = PinView.as_view()(request, self.PIN)
        self.assertEqual(response.status_code, 200)

    def test_post_pin_permission(self):
        url = "/pins/api/%s" % self.PIN
        request = self.factory.post(url)
        request.user = AnonymousUser()
        response = PinView.as_view()(request, self.PIN)

        self.assertEqual(response.status_code, 403)

        request.user = self.test_user
        response = PinView.as_view()(request, self.PIN)
        self.assertEqual(response.status_code, 200)

    def test_post_pin(self):
        url = "/pins/api/%s" % self.PIN
        data = self.api_client.post(url, {"mode": self.OUT_MODE}, format="json").data

        self.assertTrue(data.get("operation"))
        self.assertEqual(data.get("pin").get("mode"), self.OUT_MODE)
        self.assertEqual(data.get("pin").get("hr_mode"), "OUT")

        data = self.api_client.post(url, {"value": self.HIGH_VALUE}, format="json").data

        self.assertTrue(data.get("operation"))
        self.assertEqual(data.get("pin").get("value"), self.HIGH_VALUE)
        self.assertEqual(data.get("pin").get("hr_value"), "HIGH")



    def test_get_pin(self):
        url = "/pins/api/%s" % self.PIN
        data = self.api_client.get(url).data

        self.assertEqual(data.get("BCM"), 17)

    def test_write_and_get_pin(self):
        write_pin_mode(self.PIN, self.OUT_MODE)
        write_pin_value(self.PIN, self.HIGH_VALUE)
        url = "/pins/api/%s" % self.PIN

        data = self.api_client.get(url).data

        self.assertEqual(data.get("value"), self.HIGH_VALUE)
        self.assertEqual(data.get("hr_value"), "HIGH")
        self.assertEqual(data.get("mode"), self.OUT_MODE)
        self.assertEqual(data.get("hr_mode"), "OUT")















