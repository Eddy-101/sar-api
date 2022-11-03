from rest_framework.generics import ListAPIView

from .serializers import UserSerializer
from .models import User

# Create your views here.
class ListUsers(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

