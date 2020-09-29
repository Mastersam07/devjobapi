from rest_framework.test import APITestCase
from django.urls import reverse
# from faker import Faker
from accounts.models import User
from accounts.serializers import UserSerializer


class TestSetup(APITestCase):
    
    def setUp(self):
        self.register_url=reverse("register")
        self.login_url=reverse("login")
        self.token_url=reverse("token")
        # self.fake = Faker()
        
        self.user_data = {
            "email" : "d@d.com",
            "password" : "123456",
            "password2" : "123456",
            "gender" : "male",
            "role" : "employee",
        }

        self.serializer_data = {
            "email" : "d@d.com",
            "password" : "123456",
            "gender" : "male",
            "role" : "employee",
        }

        # self.user = User.objects.create(**self.serializer_data)
        # self.serializer = UserSerializer(instance=self.user)
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()