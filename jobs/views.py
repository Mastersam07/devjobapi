from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
  
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from jobs.permissions import IsEmployee
from jobs.serializers import ApplicantSerializer, JobSerializer
from jobs.models import Applicant, Job

from .serializers import *
from django.core import serializers
from django.core.serializers import serialize
import json
from django.http.response import HttpResponse


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    # queryset = serializer_class.Meta.model.objects.filter(filled=False)
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [AllowAny]


class SearchApiView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'location' in self.request.GET and 'position' in self.request.GET:
            return self.serializer_class.Meta.model.objects.filter(location__icontains=self.request.GET['location'],
                                                                   title__icontains=self.request.GET['position'])
        else:
            # return self.serializer_class.Meta.model.objects.filter(filled=False)
            return self.serializer_class.Meta.model.objects.all()


class SaveJobApiView(CreateAPIView):
    serializer_class = ApplicantSerializer
    http_method_names = [u'post']
    permission_classes = [IsAuthenticated, IsEmployee]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SavedJobsAPIView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_queryset(self):
        saved_jobs_id = list(Applicant.objects.filter(user=self.request.user).values_list('job_id', flat=True))
        return Job.objects.filter(id__in=saved_jobs_id)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEmployee])
def already_saved_job_api_view(request, job_id):
    saved_job_id = Applicant.objects.filter(job_id=job_id).values_list('job_id')
    data = serializers.serialize("json", Job.objects.filter(id__in=saved_job_id))

    return HttpResponse(data, content_type="application/json")