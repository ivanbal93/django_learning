from django.shortcuts import render
from django.db.models import Count, Case, When, Avg

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import UpdateModelMixin

from .models import City, Sight, Review, Author, AuthorSightRelation
from .serializers import (CitySerializer, SightSerializer, ReviewSerializer, AuthorSerializer,
                          AuthorSightRelationSerializer)
from .permissions import IsOwnerOrIsStaffOrReadOnly


# Create your views here.


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['id', 'name']
    search_fields = ['id', 'name']
    ordering_fields = ['name']
    ordering = ['id', ]


class SightViewSet(ModelViewSet):
    queryset = (Sight.objects.all().annotate(annotated_likes=Count(Case(When(authorsightrelation__like=True, then=1))),
                                             # rating=Avg('authorsightrelation__rating')
                                             ).order_by('id'))
    serializer_class = SightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['id', 'name', 'city__id', 'city__name']
    search_fields = ['id', 'name', 'city__id', 'city__name']
    ordering_fields = ['name', 'city__id', 'city__name']
    ordering = ['id']


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrIsStaffOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = ['id', 'name', 'gender']
    search_fields = ['id', 'name', 'gender']
    ordering_fields = ['name']
    ordering = ['id', ]


class AuthorSightRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AuthorSightRelation.objects.all()
    serializer_class = AuthorSightRelationSerializer
    lookup_field = 'author_sight'

    def get_object(self):
        obj, _ = AuthorSightRelation.objects.get_or_create(user=self.request.user,
                                                           sight=self.kwargs['author_sight'])
        return AuthorSightRelation.objects.get(id=self.request.id)
