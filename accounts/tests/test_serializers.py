from .test_setup import TestSetup
from ..models import User
from accounts.serializers import UserCreateSerializer, UserSerializer


class TestSerializers(TestSetup):

    """Testing user creation serializer"""
    def test_user_contains_expected_fields(self):
        self.serializer_data = {
            "email" : "d@d.com",
            "password" : "123456",
            "gender" : "male",
            "role" : "employee",
        }

        self.user = User.objects.create(**self.serializer_data)
        self.serializer = UserSerializer(instance=self.user)

        data = (self.serializer).data

        self.assertTrue(any(field in set(data.keys()) for field in set(["email", "password", "gender", "role"])))    