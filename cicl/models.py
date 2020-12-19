from django.db import models
from django.core.validators import RegexValidator

import re
import uuid


# Regex Validator
alphabet_regex = RegexValidator(
  r'^[A-Za-z\-\.]+$',
  'Only alphabet characters are allowed.'
)


# Isotope model
class Isotope(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    symbol = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def clean(self):
        self.name = re.sub(' +', ' ', self.name)
        self.name = self.name.title()
        self.symbol = self.symbol.capitalize()

    def __str__(self):
        return '{} - {}'.format(self.name, self.symbol)


# Parameter model
class Parameter(models.Model):
    type = models.CharField(
        max_length=30,
        primary_key=True,
        validators=[alphabet_regex]
    )

    class Meta:
        ordering = ['type']

    def clean(self):
        self.type = re.sub(' +', ' ', self.type)
        self.type = self.type.title()

    def __str__(self):
        return self.type


# Researcher model
class Researcher(models.Model):
    researcher_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    first_name = models.CharField(max_length=30, validators=[alphabet_regex])
    last_name = models.CharField(max_length=50, validators=[alphabet_regex])
    email = models.EmailField(max_length=70, blank=True)

    class Meta:
        ordering = ['last_name']

    def clean(self):
        self.first_name = re.sub(' +', ' ', self.first_name)
        self.last_name = re.sub(' +', ' ', self.last_name)
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


# Document model
class Document(models.Model):
    document_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    document_file = models.FileField(upload_to='document/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    core_name = models.CharField(max_length=50)
    year = models.IntegerField()
    age_range_start = models.CharField(max_length=12)
    age_range_end = models.CharField(max_length=12)
    researchers = models.ManyToManyField(Researcher)
    isotopes = models.ManyToManyField(Isotope)
    parameters = models.ManyToManyField(Parameter)

    class Meta:
        ordering = ['core_name']
