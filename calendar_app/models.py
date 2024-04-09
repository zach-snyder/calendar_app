from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length = 100)
    start_time = models.DateTimeField(default = timezone.localtime)
    end_time = models.DateTimeField(default=timezone.localtime)
    description = models.TextField(blank = True)
    location = models.CharField(max_length = 250, blank = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', args=[str(self.id)])