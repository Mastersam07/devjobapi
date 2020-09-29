from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from accounts.models import User

JOB_TYPE = (
    ('Full Time', "Full Time"),
    ('Part time', "Part time"),
    ('Part time', "Internship"),
)

DEFAULT_TAG = (
    ("General", 'software'),
    ("Obvious", 'tech'),
)

def get_tag_default():
    return list(dict(DEFAULT_TAG).values())


class Job(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10, default="Full Time")
    # category = models.CharField(max_length=100)
    last_date = models.DateTimeField(null=True, blank=True)
    company_name = models.CharField(max_length=100)
    # company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    # created_at = models.DateTimeField(default=timezone.now)
    # filled = models.BooleanField(default=False)
    # salary = models.IntegerField(default=0, blank=True)
    tags = ArrayField(models.CharField(max_length=200),default=get_tag_default, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    # created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'job']

    def __str__(self):
        return self.user.get_full_name()