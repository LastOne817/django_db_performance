from django.db import models


class Sample(models.Model):
    content = models.CharField(max_length=32)
