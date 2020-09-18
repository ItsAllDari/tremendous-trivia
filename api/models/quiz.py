from django.db import models
# from django.contrib.auth.models import User

class Quiz(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=70)
  image = models.ImageField()
  slug = models.SlugField(blank=True)
  roll_out = models.BooleanField(default=False)
  timestamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['timestamp',]
    verbose_name_plural = "Quizzes"

  def __str__(self):
    return self.name

  # def __init__(self, prompt, answer):
  #   self.prompt = prompt
  #   self.answer = answer
