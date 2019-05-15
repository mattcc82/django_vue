import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer
from profiles.models import Profile, ProfileStatus


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {}
        data['username'] = 'testcase'
        data['email'] = 'test@gongos.com'
        data['password1'] = 'G0ng0s_!!_!!'
        data['password2'] = 'G0ng0s_!!_!!'

        response = self.client.post('/api/rest-auth/registration/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='newGuy',
            password='G0ng0s_!!_!!'
        )
        self.token = Token.objects.create(
            user=self.user
        )
        self.api_auth()

    def api_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_profile_list_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_not_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile-detail', kwargs={ 'pk': 1 }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'newGuy')

    def test_profile_update_by_owner(self):
        response = self.client.put(
            reverse('profile-detail', kwargs={'pk': 1}),
            { 
                'city': 'TestCity',
                'bio': 'Test_Bio' 
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            { 
                'id': 1,
                'user': 'newGuy',
                'bio': 'Test_Bio',
                'city': 'TestCity',
                'avatar': None
            }
        )
    
    def test_profile_update_by_random(self):
        random_user = User.objects.create_user(
            username='anon',
            password='asdASD_ASD_!!'
        )
        self.client.force_authenticate(user=random_user)
        response = self.client.put(
            reverse('profile-detail', kwargs={'pk': 1}),
            {
                'city': 'random_city!',
                'bio': 'random_bio!'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

class ProfileStatusViewSetTestCase(APITestCase):

    url = reverse('status-list')

    def setUp(self):
        self.user = User.objects.create_user(
            username='newGuy',
            password='G0ng0s_!!_!!'
        )
        self.status = ProfileStatus.objects.create(
            user_profile=self.user.profile,
            status_content='status test'
        )
        self.token = Token.objects.create(
            user=self.user
        )
        self.api_auth()

    def api_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_status_list_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_not_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {}
        data['status_content'] = 'testing new status'
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_profile'], 'newGuy')
        self.assertEqual(response.data['status_content'], 'testing new status')

    def test_single_status_get(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse('status-detail', kwargs={ 'pk': 1 }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)
    
    def test_status_update_owner(self):
        data = {}
        data['status_content'] = 'testing content update'
        response = self.client.put(reverse('status-detail', kwargs={ 'pk': 1 }), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status_content'], 'testing content update')
    
    def test_status_update_random(self):
        random_user = User.objects.create_user(
            username='anon',
            password='asdASD_ASD_!!'
        )
        self.client.force_authenticate(user=random_user)
        data = {}
        data['status_content'] = 'testing content update - random user!!!'
        response = self.client.put(reverse('status-detail', kwargs={ 'pk': 1 }), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
