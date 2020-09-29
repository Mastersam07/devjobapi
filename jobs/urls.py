from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('jobs', JobViewSet)

urlpatterns = [
    path('search/', SearchApiView.as_view()),
    path('save-job/<int:job_id>', SaveJobApiView.as_view()),
    path('saved-jobs', SavedJobsAPIView.as_view()),
    path('saved-job/<int:job_id>', already_saved_job_api_view),
]

urlpatterns += router.urls