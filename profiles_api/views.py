from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditiona django view',
            'Gives you the most control over your aplication logic',
            'Is mapped manually to URls',
        ]

        return Response({'message':'hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """"Create a hello message with our name"""
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                )
            
    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'method':'PUT'})

    def patch(self, requet, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Deleting an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions(list, create, retrive, update, partial_update)',
            'Automaatically maps to urls using routers',
            'Provides more functonaliity with less code',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """Create new hello message"""
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """"Handle updating object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """"Handle updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """"Handle removing an object"""
        return Response({'http_method':'DELETE'})
