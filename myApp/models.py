from django.db import models
from datetime import datetime

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    opening_time = models.TimeField()
    closing_time = models.TimeField()


    def is_open(self):
        current_time = datetime.now().time()
        return self.opening_time <= current_time <= self.closing_time

