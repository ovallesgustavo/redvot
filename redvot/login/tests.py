# from django.test import TestCase

# Create your tests here.
# from functools import partial

from rest_framework.test import APITestCase

# from rest_framework.reverse import reverse
# from rest_framework_simplejwt.exceptions import TokenError
# from rest_framework_simplejwt.tokens import RefreshToken

# from apps.account.models import User


class TestLoginCase(APITestCase):

    # login_url = reverse('login')
    """
    refresh_token_url = reverse('token_refresh')
    logout_url = reverse('logout')

    email = 'test@user.com'
    password = 'kah2ie3urh4k'

    def setUp(self):
        user = User.objects.get(self.email, self.password)

    def _login(self):
        data = {
            'email': self.email, 'password': self.password
        }
        r = self.client.post(self.login_url, data)
        body = r.json()
        if 'access' in body:
            self.client.credentials(
                HTTP_AUTHORIZATION='Bearer %s' % body['access'])
        return r.status_code, body
    """
    # print('|||| ',login_url)
    pass
