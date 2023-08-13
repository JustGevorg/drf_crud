from django.http import Http404
from rest_framework.views import APIView
from django.db import models

# Create your views here.


class InstanceAvailbilitySafeAPIView(APIView):
    def get_object(self, pk, model: models.Model):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404
