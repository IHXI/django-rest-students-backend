from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    favorite_emoji = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

