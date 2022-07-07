from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditiona django view',
            'Gives you the most control over your aplication logic',
            'Is mapped manually to URls',
        ]

        return Response({'message':'hello!', 'an_apiview': an_apiview})

