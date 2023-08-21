from django.db.models import Avg

from .models import Sight, AuthorSightRelation


def set_rating(sight):
    sight.rating = AuthorSightRelation.objects.filter(sight=sight).aggregate(rating=Avg('rating')).get('')
    sight.save()
