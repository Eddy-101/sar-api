from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ListAllEndpoints(APIView):

    def get(self, request, format=None):
        urls = {
            '/api/v1/users',
            '/admin',
        }
        return Response({'v1':urls})
