from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectView(APIView):
    def get(self, request, client_id):
        projects = Project.objects.filter(client_id=client_id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, client_id):
        request.data['client'] = client_id
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)