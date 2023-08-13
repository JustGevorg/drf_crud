from django.http import Http404
from rest_framework import generics, response, status, viewsets
from rest_framework.views import APIView
from facilities_area.models import MasterProfile, Event, Task
from facilities_area.serializers import (
    MasterProfileModelSerializer,
    EventSerializer,
    TaskModelSerializer,
)
from common.views import InstanceAvailbilitySafeAPIView


class MasterProfilesAPIView(generics.ListAPIView):
    queryset = MasterProfile.objects.all()  # use exclude in serializer instead defer!
    serializer_class = MasterProfileModelSerializer


class EventAPIView(InstanceAvailbilitySafeAPIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        if pk:
            target_event = self.get_object(pk=pk, model=Event)

            serializer = EventSerializer(target_event)
            return response.Response(serializer.data)

        serializer = EventSerializer(Event.objects.all(), many=True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data)

    def put(self, request, *args, **kwargs):
        updatable_event = self.get_object(pk=self.kwargs.get("pk"), model=Event)
        serializer = EventSerializer(data=request.data, instance=updatable_event)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        deletable_event = self.get_object(pk=self.kwargs.get("pk"), model=Event)
        deletable_event.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
