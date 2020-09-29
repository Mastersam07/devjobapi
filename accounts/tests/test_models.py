from .test_setup import TestSetup
from ..models import User


class TestModels(TestSetup):

    """Test all models"""
    def test_user_has_an_email(self):
        user = User.objects.create(**self.serializer_data)
        self.assertEqual(str(user.email), "d@d.com")
    
    def test_user_has_an_gender(self):
        user = User.objects.create(**self.serializer_data)
        self.assertEqual(str(user.gender), "male")
    
    def test_user_has_a_role(self):
        user = User.objects.create(**self.serializer_data)
        self.assertEqual(str(user.role), "employee")
    
