from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="DevJobHubApi",
      default_version='v1',
      description="DevJobHub Api Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="abadasamuelosp@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('jobs.urls')),
    path('', include('accounts.urls')),
    path('api/v1/', include([
        path('swagger', schema_view.with_ui('swagger', cache_timeout=0)),
        path('', include('accounts.urls')),
        path('', include('jobs.urls')),
    ])),
]