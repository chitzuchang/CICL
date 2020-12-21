from rest_framework import serializers

from .models import Document, Isotope, Parameter, Researcher


# Isotope Serializer
class IsotopeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    symbol = serializers.CharField(max_length=20)

    class Meta:
        model = Isotope
        fields = (
            'name',
            'symbol',
        )


# Parameter Serializer
class ParameterSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=30)

    class Meta:
        model = Parameter
        fields = (
            'type',
        )


# Researcher Serializer
class ResearcherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=70)

    class Meta:
        model = Researcher
        fields = (
            'researcher_id',
            'first_name',
            'last_name',
            'email',
        )


# Document Serializer
class DocumentSerializer(serializers.ModelSerializer):
    location = serializers.CharField(max_length=50)
    core_name = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    age_range_start = serializers.CharField(max_length=12)
    age_range_end = serializers.CharField(max_length=12)
    researchers = ResearcherSerializer(many=True)
    isotopes = IsotopeSerializer(many=True)
    parameters = ParameterSerializer(many=True)

    class Meta:
        model = Document
        fields = (
            'document_id',
            'document_file',
            'created',
            'location',
            'core_name',
            'year',
            'age_range_start',
            'age_range_end',
            'researchers',
            'isotopes',
            'parameters',
        )
        read_only_fields = ('document_id', 'created')
