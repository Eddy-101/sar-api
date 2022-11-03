from django.contrib import admin

from .models import (User, UserCondition) 

# Register your models here.
admin.site.register(User)
admin.site.register(UserCondition)
