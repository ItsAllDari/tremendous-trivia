from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from .user import User
from django.dispatch import receiver
from django.template.defaultfilters import slugify

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

class Question(models.Model):
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  label = models.CharField(max_length=100)
  order = models.IntegerField(default=0)

  def __str__(self):
    return self.label

class Answer (models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  label = models.CharField(max_length=100)
  is_correct = models.BooleanField(default=False)

  def __str__(self):
    return self.label

class Player(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  score = models.IntegerField(default=0)
  completed = models.BooleanField(default=False)
  date_finished = models.DateTimeField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.email

class PlayerAnswer(models.Model):
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

  def __str__(self):
    return self.question.label

@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
  instance.slug = slugify(instance.name)
