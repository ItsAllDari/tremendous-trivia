from django.db import models
# from django.contrib.auth.models import User

class Answer (models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  label = models.CharField(max_length=100)
  is_correct = models.BooleanField(default=False)

  def __str__(self):
    return self.question.label
