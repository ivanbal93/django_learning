from django.test import TestCase

from data.rating import set_rating
from data.models import Sight, City


class SetRatingTestCase(TestCase):
    def setUp(self) -> None:
        self.city_1 = City.objects.create(
            name='city',
            description='city description',
            coordinates='https://goo.gl/maps/city'
        )
        self.sight_1 = Sight.objects.create(
            name='sight',
            description='sight description',
            coordinates='https://goo.gl/maps/sight',
            city=self.city_1,
        )

    def test_ok(self):
        print(set_rating(self.sight_1))