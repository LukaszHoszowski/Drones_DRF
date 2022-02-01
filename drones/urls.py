from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import DroneCategoryViewSet, PilotViewSet

app_name = 'drones'

# router = SimpleRouter()
# router.register('drone-categories', DroneCategoryViewSet, basename='drone-categories')
# # router.register('drones', DroneViewSet, basename='drones')
# router.register('pilots', PilotViewSet, basename='pilots')
# router.register('competitions', CompetitionViewSet, basename='competitions')
#
# urlpatterns = router.urls

urlpatterns = [
    path('drones/', views.DroneList.as_view(), name='drones'),
    path('drones/<int:pk>/', views.DroneDetail.as_view(), name='drones-detail'),

    path('competitions/', views.CompetitionList.as_view(), name='competitions'),
    path('competitions/<int:pk>/', views.CompetitionDetail.as_view(), name='competition-detail'),
]
