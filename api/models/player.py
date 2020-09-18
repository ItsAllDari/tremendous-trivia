from django.db import models
# from django.contrib.auth.models import User

class Player(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  score = models.IntegerField(default=0)
  completed = models.BooleanField(default=False)
  date_finished = models.DateTimeField()
  timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.user.username
