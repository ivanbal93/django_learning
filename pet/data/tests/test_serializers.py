from django.test import TestCase

from rest_framework.renderers import JSONRenderer

from data.serializers import CitySerializer
from data.models import City


class CitySerializerTestCase(TestCase):
    def test_passed(self):
        test_1 = City.objects.create(name='test_1')
        test_2 = City.objects.create(name='test_2')
        data = CitySerializer([test_1, test_2], many=True).data
        expected_data = [
            {
                'id': test_1.id,
                'name': 'test_1',
                'description': ''
            },
            {
                'id': test_2.id,
                'name': 'test_2',
                'description': ''
            }
        ]
        self.assertEqual(expected_data, data)
