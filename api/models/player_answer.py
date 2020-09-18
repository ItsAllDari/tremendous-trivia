from django.db import models
# from django.contrib.auth.models import User

class PlayerAnswer(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
