from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Todo(models.Model):
#     fecha_creado = models.DateTimeField(auto_now=True)
#     fecha_finalizado = models.DateTimeField(blank=True, null=True)
#     todo = models.TextField(default=0)
#     hecho = models.BooleanField(default=False)
#
#     def __unicode__(self):
#         return self.fecha_creado
#
# class Currencies(models.Model):
#     currency_name = models.CharField(max_length=200, null=True)
#     short_name = models.CharField(max_length=200, default=0)
#
#     def __unicode__(self):
#         return self.currency_name