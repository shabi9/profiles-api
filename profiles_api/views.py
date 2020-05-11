from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """api view class"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return list of api views features"""
        an_apiview = [
             'Uses http functions (get, post, patch, delete)',
             'Is similar to traditional djnago view',
             'gives you the most control over you app logic',
             'is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a post method"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})
