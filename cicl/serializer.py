from rest_framework import serializers
from .models import Document

# Document Serializer
class DocumentSerializer(serializers.ModelSerializer):
  location = serializers.CharField(max_length=50)
  core_name = serializers.CharField(max_length=50)
  year = serializers.IntegerField()
  age_range_start = serializers.CharField(max_length=12)
  age_range_end = serializers.CharField(max_length=12)
  researchers = serializers.JSONField()
  isotopes = serializers.JSONField()
  parameters = serializers.JSONField()

  class Meta:
    model = Document 
    fields = ('document_id', 'location', 'core_name', 'year', 'age_range_start', 'age_range_end', 'researchers', 'isotopes', 'parameters',)
    read_only_fields = ('document_id',)

