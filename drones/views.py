from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import DroneCategory, Drone, Pilot, Competition
from .serializers import DroneCategorySerializer, DroneSerializer, PilotSerializer, CompetitionSerializer


class DroneCategoryViewSet(ModelViewSet):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


# class DroneViewSet(ModelViewSet):
#     queryset = Drone.objects.all()
#     serializer_class = DroneSerializer


class PilotViewSet(ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer


# class CompetitionViewSet(ModelViewSet):
#     queryset = Competition.objects.all()
#     serializer_class = CompetitionSerializer


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


class CompetitionDetail(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
