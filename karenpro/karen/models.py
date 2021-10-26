from django.db import models

# Create your models here.
class word(models.Model):
    Word_th = models.CharField(max_length = 100)
    Sound = models.CharField(max_length = 100)

def __str__(self):
    return self.name

class questions(models.Model):
    Question = models.CharField(max_length = 100)
    Sound = models.CharField(max_length = 100)
    Type = models.IntegerField()

def __str__(self):
    return self.name
    
class choice(models.Model):
    Choice = models.CharField(max_length = 50)
    Icon = models.CharField(max_length = 60,null=True)
    Sound = models.CharField(max_length = 100)
    Question_id = models.IntegerField()

def __str__(self):
    return self.name