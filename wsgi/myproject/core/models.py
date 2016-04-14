from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    fecha_creado = models.DateTimeField(auto_now=True)
    fecha_finalizado = models.DateTimeField()
    propietario = models.ForeignKey(User)
    why = models.CharField(max_length=200,null=True)

    def __unicode__(self):
        return self.why