import json

from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from django.urls import reverse
from django.contrib.auth.models import User

from data.models import City, Sight, Review
from data.serializers import CitySerializer, SightSerializer, ReviewSerializer


class CityViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user')
        self.test_1 = City.objects.create(name='test_1', description='')
        self.test_2 = City.objects.create(name='test_2', description='')
        self.test_3 = City.objects.create(name='test_3', description='test_1')
        self.url = reverse('city-list')

    def test_get(self):
        response = self.client.get(self.url)
        serializer_data = CitySerializer([self.test_1, self.test_2, self.test_3, ], many=True).data
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    # def test_filter(self):
    #     response = self.client.get(self.url, data={'name': '1'})
    #     serializer_data = CitySerializer([self.test_1, ], many=True).data
    #     self.assertEqual(HTTP_200_OK, response.status_code)
    #     self.assertEqual(serializer_data, response.data)

    def test_search(self):
        response = self.client.get(self.url, data={'search': '3'})
        serializer_data = CitySerializer([self.test_3, ], many=True).data
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, City.objects.all().count())
        data = {
            'name': 'test_1',
            'description': 'test_1',
            'coordinates': 'https://goo.gl/maps/4MPF3JijQUnXHSip6'
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.post(self.url, data=json_data, content_type='application/json')
        self.assertEqual(HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, City.objects.all().count())

    def test_update(self):
        self.url = reverse('city-detail', args=(self.test_1.id, ))
        data = {
            'name': 'test_2',
            'description': 'test_2',
            'coordinates': 'https://goo.gl/maps/4MPF3JijQUnXHSip6'
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.put(self.url, data=json_data, content_type='application/json')
        self.test_2.refresh_from_db()
        self.assertEqual(HTTP_200_OK, response.status_code)


class SightViewSetTestCase(APITestCase):
    def test_get(self):
        test_1 = Sight.objects.create(name='sight_1')
        test_2 = Sight.objects.create(name='sight_2')
        url = reverse('sight-list')
        response = self.client.get(url)
        print(response.data)
        serializer_data = SightSerializer([test_1, test_2], many=True).data
        self.assertEqual(serializer_data, response.data)

#
#
# class ReviewViewSetTestCase(APITestCase):
#     def test_get(self):
#         test_1 = Review.objects.create(text='review_1')
#         test_2 = Review.objects.create(text='review_2')
#         url = reverse('review-list')
#         response = self.client.get(url)
#         serializer_data = ReviewSerializer([test_1, test_2], many=True).data
#         self.assertEqual(serializer_data, response.data)
