from rest_framework.routers import SimpleRouter

from .views import DroneCategoryViewSet, DroneViewSet, PilotViewSet, CompetitionViewSet

app_name = 'drones'

router = SimpleRouter()
router.register('drone-categories', DroneCategoryViewSet, basename='drone-categories')
router.register('drones', DroneViewSet, basename='drones')
router.register('pilots', PilotViewSet, basename='pilots')
router.register('competitions', CompetitionViewSet, basename='competitions')

urlpatterns = router.urls
