from .test_setup import TestSetup
from ..models import User


class TestViews(TestSetup):
    
    """Tests with regards to registration"""
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEquals(res.status_code, 400)
    
    def test_user_can_register_with_correct_data(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEquals(res.status_code, 201)
        
    """Tests with regards to login"""
    def test_user_cannot_login_with_unverified_email(self):
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEquals(res.status_code, 401)
    
    def test_user_can_login_with_after_verification(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data["email"]
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEquals(res.status_code, 200)
    
    """Tests with regards to token"""
    def test_user_cannot_refresh_token_with_no_data(self):
        res = self.client.post(self.token_url)
        self.assertEquals(res.status_code, 400)
    
    def test_user_can_refresh_token_with_data(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data["email"]
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        resp = self.client.post(self.login_url, self.user_data, format="json")
        self.user_token = {
            "token" : resp.data["access"],
            "refresh" : resp.data["refresh"],
        }
        res = self.client.post(self.token_url, self.user_token, format="json")
        self.assertEquals(res.status_code, 200)