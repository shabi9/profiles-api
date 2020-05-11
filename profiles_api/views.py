from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """api view class"""

    def get(self, request, format=None):
        """return list of api views features"""
        an_apiview = [
             'Uses http functions (get, post, patch, delete)',
             'Is similar to traditional djnago view',
             'gives you the most control over you app logic',
             'is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
