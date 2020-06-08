from django.db import models


class Introduction(models.Model):
    option = models.PositiveIntegerField(default=0)


class Question(models.Model):
    number = models.PositiveIntegerField()
    condition = models.TextField()
    introduction = models.ForeignKey(Introduction, on_delete = models.CASCADE, related_name = 'question')
    first_choice = models.CharField(max_length = 100)
    second_choice = models.CharField(max_length = 100)
    third_choice = models.CharField(max_length = 100)
    fourth_choice = models.CharField(max_length = 100)
    right_choice = models.CharField(max_length = 100)
    


    

