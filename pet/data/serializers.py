from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField, DecimalField, CharField
from .models import City, Sight, Review, Author, AuthorSightRelation

from django.db.models import When, Count, Case


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SightSerializer(ModelSerializer):
    # likes_count = SerializerMethodField()
    annotated_likes = IntegerField()
    rating = DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        model = Sight
        fields = (
            'name',
            'description',
            'coordinates',
            # 'likes_count',
            'annotated_likes',
            'rating'
        )

    def get_likes_count(self, instance):
        return AuthorSightRelation.objects.filter(sight=instance, like=True).count()


class ReviewSerializer(ModelSerializer):
    author = CharField(source='author.username', default='', read_only=True)

    class Meta:
        model = Review
        fields = [
            'text',
            'coordinates',
            'author'
        ]


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'name',
            'gender'
        ]


class AuthorSightRelationSerializer(ModelSerializer):
    class Meta:
        model = AuthorSightRelation
        fields = [
            'sight',
            'like',
            'rating'
        ]
