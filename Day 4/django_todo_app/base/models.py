from django.db import models
#  Import user Model
from django.contrib.auth.models import User, User
from django.db.models.fields import CharField

# Create your models here.

#  Creatsing our Database Table

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # This create a text box

    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    # st
    def __str__(self):
        return self.title

    #  Self ordering
    class Meta:
        ordering = ['complete']
