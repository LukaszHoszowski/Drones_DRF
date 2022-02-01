from rest_framework import serializers

from .models import DroneCategory, Drone, Pilot, Competition


class DroneCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneCategory
        fields = ('name', 'pk')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='drone:drone-detail', lookup_field='pk')
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

    # to musi byc bo jest app_name w urlsach

    class Meta:
        model = Drone
        fields = ('url', 'name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp')
        # lookup_field = ('pk',)
        # depth = 1
        # read_only_fields = ('name', )


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ('name', 'gender', 'races_count', 'inserted_timestamp', 'pk')


# class CompetitionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Competition
#         fields = ('pilot', 'drone', 'distance', 'achievement_date', 'pk')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    # drone = DroneSerializer()

    # nazwa modelu -detail

    class Meta:
        model = Competition
        fields = ('url', 'distance', 'achievement_date', 'drone')
        extra_kwargs = {
            "url": {
                "view_name": "drone:competition-detail",
                "lookup_field": "pk"
            },
            "drone": {
                "view_name": "drone:drone-detail",
                "lookup_field": "pk"
            }
        }
