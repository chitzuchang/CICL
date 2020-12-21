from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import DocumentSerializer
from .models import Document


# Main Page View
def MainPage(request):
    return render(request, template_name='index.html')


# Pagination
class DocumentViewPagination(LimitOffsetPagination):
    default_limit = 12
    max_limit = 12


# Document Views
class GetAllDocumentAPIView(ListAPIView):
    permission_classes = [AllowAny]

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = (
        'location',
        'core_name',
        'researchers__first_name',
        'researchers__last_name',
        'isotopes__name',
        'parameters__type'
    )
    pagination_class = DocumentViewPagination


class DocumentAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        document = Document.objects.get(pk=pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data, status=status.HTTP_200_OK)
