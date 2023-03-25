from django.db import models
from core.models import Base

# Create your models here.
from django.db import models
from core.models import Base

class Project(Base):
    link = models.URLField()
    picture = models.ImageField(upload_to='project_pictures/')
    description = models.TextField()

    def __str__(self):
        return f"{self.display_name} - {self.link}"
