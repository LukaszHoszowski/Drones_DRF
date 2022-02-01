from rest_framework import serializers

from .models import DroneCategory, Drone, Pilot, Competition


class DroneCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneCategory
        fields = ('name', 'pk')


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp', 'pk')


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ('name', 'gender', 'races_count', 'inserted_timestamp', 'pk')


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('pilot', 'drone', 'distance', 'achievement_date', 'pk')
