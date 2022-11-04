from django.urls import path 

from .views import * 

app_name = 'users'

urlpatterns = [
    path('', ListUsers.as_view(), name="users_list"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', LoginUser.as_view(), name="login"),
]
