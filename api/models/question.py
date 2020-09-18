from django.db import models
# from django.contrib.auth.models import User
from .quiz import Quiz

class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  label = models.CharField(max_length=100)
  order = models.IntegerField(default=0)

  def __str__(self):
    return self.label
