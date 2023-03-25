from django.db import models
from core.models import Base 
# Create your models here.

class Testimonial(Base):
    message = models.TextField()
    occupation = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.occupation + ' - ' + self.message[:20]
