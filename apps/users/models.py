from django.db import models

from .managers import UserManager
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.utils import timezone

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    state_choices = (
        ('s', 'Saludable'),
        ('r', 'Regular'),
        ('i', 'Insaludable')
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='users', blank=True, null=True)
    surname = models.CharField(max_length=50)
    objective_weight = models.PositiveIntegerField(default=0)
    state = models.CharField(max_length=1, choices=state_choices) 
    description = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Usuario',
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.id} - {self.name}"


class Status(models.Model):
    date = models.DateField(default=timezone.now())
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    hip = models.FloatField(default=0)
    waist = models.FloatField(default=0)
    minimum_pressure = models.FloatField(default=0)
    maximum_pressure = models.FloatField(default=0)
    imc = models.FloatField(default=0)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Condicion Fisica'
        verbose_name_plural = 'Condiciones Fisicas'

    def __str__(self): 
        return f"{self.id} - {self.date}"
