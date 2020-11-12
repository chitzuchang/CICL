from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import DocumentSerializer
from .models import Document

# Document Views 
class GetAllDocumentAPIView(APIView):
  permission_classes = [AllowAny]

  def get(self, request, format=None):
    documents = Document.objects.all()
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

class DocumentAPIView(APIView):
  permission_classes = [AllowAny]

  def get(self,request, pk, format=None):
    document = Document.objects.get(pk=pk)
    serializer = DocumentSerializer(document) 
    return Response(serializer.data, status=status.HTTP_200_OK)





