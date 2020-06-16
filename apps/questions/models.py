from django.db import models
from django.contrib.auth.models import User

from apps.users.models import Profile

from ckeditor.fields import RichTextField


RIGHT_ANSWER_CHOICE = [
    ('а_вариант', 'А_ВАРИАНТ'),
    ('б_вариант', 'Б_ВАРИАНТ'),
    ('в_вариант', 'В_ВАРИАНТ'),
    ('г_вариант', 'Г_ВАРИАНТ'),
    ('д_вариант', 'Д_ВАРИАНТ'),
    ]

class Introduction(models.Model):
    номер = models.PositiveIntegerField()
    имя = models.CharField(max_length = 255)
    введение = models.TextField() 

class Question(models.Model):
    номер = models.PositiveIntegerField()
    картинка = models.ImageField(upload_to = 'questionImages', null = True, blank = True)
    условие= RichTextField(null = True, blank = True)
    введение = models.ForeignKey(Introduction, on_delete = models.CASCADE, related_name = 'question')
    a_вариант = RichTextField(null = True, blank = True)
    б_вариант = RichTextField(null = True, blank = True)
    в_вариант = RichTextField(null = True, blank = True)
    г_вариант = RichTextField(null = True, blank = True)
    д_вариант = RichTextField(null = True, blank = True)
    правильный_вариант = models.CharField(max_length = 100, choices = RIGHT_ANSWER_CHOICE)
    объяснение = RichTextField(null = True, blank = True)


    def __str__(self):
        return f"question of {self.номер}"


class Review(models.Model):
    профайл = models.ForeignKey(Profile, on_delete = models.CASCADE, null = True, blank = True, related_name = 'review')
    введение = models.ManyToManyField(Introduction)
    балл = models.PositiveIntegerField(default = 0)


class Answer(models.Model):
    вопрос = models.ForeignKey(Question, on_delete = models.CASCADE, null = True, blank = True)
    отмеченный_вариант = models.CharField(max_length = 100, choices = RIGHT_ANSWER_CHOICE, null = True, blank = True)
    просмотр = models.ForeignKey(Review, on_delete = models.CASCADE, related_name = 'answer', null = True, blank = True)





    

