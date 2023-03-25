from django.db import models

# Create your models here.
from django.db import models
from core.models import Base

class Message(Base):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.subject} from {self.email}"
