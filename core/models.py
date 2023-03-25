from django.db import models

# Create your models here.
from django.db import models


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    display_name = models.CharField(max_length=255)

    class Meta:
        abstract = True
