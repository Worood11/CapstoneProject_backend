from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTests(APITestCase):
    def setUp(self):
        """Set up test client and create test user"""
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.register_url = reverse('signup')
        self.login_url = reverse('login')
        self.token_refresh_url = reverse('token_refresh')

    def test_user_registration_success(self):
        """Test successful user registration"""
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_registration_invalid_data(self):
        """Test user registration with invalid data"""
      
        data = {'username': 'incomplete'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_user_login_success(self):
        """Test successful user login"""
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        response = self.client.post(self.login_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)

    def test_user_login_invalid_credentials(self):
        """Test login with invalid credentials"""
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_refresh(self):
        """Test token refresh functionality"""
        
        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        login_response = self.client.post(self.login_url, login_data, format='json')

      
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {login_response.data["access"]}')

    
        response = self.client.get(self.token_refresh_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)

    def test_authentication_required_endpoints(self):
        """Test bookstore endpoint access with IsAdminUserOrReadOnly"""
        bookstores_url = reverse('bookstore-index')

      
        response = self.client.get(bookstores_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        post_data = {"name": "Test Store", "location": "City"}
        response = self.client.post(bookstores_url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


        login_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        login_response = self.client.post(self.login_url, login_data, format='json')
        token = login_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

     
        response = self.client.get(bookstores_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(bookstores_url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def tearDown(self):
        """Clean up after each test"""
        self.client.credentials()
