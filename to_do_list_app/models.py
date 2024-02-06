from django.db import models
from django.urls import reverse


class ToDoItems(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("description", kwargs={"pk": self.pk})


# Create your models here.
