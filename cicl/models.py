from django.db import models

import uuid

# Document model 
class Document(models.Model):
  document_id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False,
    unique=True)
  
  location = models.CharField(max_length=50)
  core_name = models.CharField(max_length=50)
  year = models.IntegerField()
  age_range_start = models.CharField(max_length=12)
  age_range_end = models.CharField(max_length=12)
  researchers = models.JSONField(null=True)
  isotopes = models.JSONField(null=True)
  parameters = models.JSONField(null=True)
