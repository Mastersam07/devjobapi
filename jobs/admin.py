from django.contrib import admin

from .models import Applicant, Job

admin.site.register(Applicant)
admin.site.register(Job)
