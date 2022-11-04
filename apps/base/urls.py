from django.urls import path

from .views import ListAllEndpoints

urlpatterns = [
    path('', ListAllEndpoints.as_view(), name="list_endpoints"),
]
