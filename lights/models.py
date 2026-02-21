from django.db import models

class LightPassport(models.Model):
    light_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.light_id
