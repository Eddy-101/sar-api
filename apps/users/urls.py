from django.urls import path 

from .views import * 

app_name = 'users'

urlpatterns = [
    path('', ListUsers.as_view(), name="users_list"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('status/', StatusView.as_view(), name="status"),
    path('login/', LoginUser.as_view(), name="login"),
    path('user/', UserView.as_view(), name="user")
]
