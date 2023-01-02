from django.db import models


class Todo(models.Model):
    item = models.CharField(max_length=255)
    status = models.IntegerField(default=1, choices=(
        (1, 'in Progress'),
        (2, 'Deleted'),
        (3, 'Fineshed'),
    ))