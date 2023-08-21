from rest_framework.routers import SimpleRouter

from .views import CityViewSet, SightViewSet, ReviewViewSet, AuthorSightRelationView


router = SimpleRouter()

router.register('api/city', CityViewSet)
router.register('api/sight', SightViewSet)
router.register('api/review', ReviewViewSet)
router.register('api/author_sight', AuthorSightRelationView)
