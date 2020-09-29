from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import *


class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"


class ApplicantSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Applicant
        fields = "__all__"