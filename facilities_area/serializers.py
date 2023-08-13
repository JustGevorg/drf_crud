from rest_framework import serializers
from facilities_area.models import MasterProfile, Task
from facilities_area.services import EventService


class MasterProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProfile
        exclude = ("skills",)


class EventSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=125)
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(required=False)

    def create(self, validated_data):
        service = EventService()

        return service.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.description = validated_data.get("description", instance.description)
        instance.save()

        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
