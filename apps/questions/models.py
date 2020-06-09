from django.db import models
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
    балл = models.PositiveIntegerField(default = 0)

class Question(models.Model):
    номер = models.PositiveIntegerField()
    условие= models.TextField()
    введение = models.ForeignKey(Introduction, on_delete = models.CASCADE, related_name = 'question')
    a_вариант = models.CharField(max_length = 100, null = True, blank = True)
    б_вариант = models.CharField(max_length = 100, null = True, blank = True)
    в_вариант = models.CharField(max_length = 100, null = True, blank = True)
    г_вариант = models.CharField(max_length = 100, null = True, blank = True)
    д_вариант = models.CharField(max_length = 100, null = True, blank = True)
    правильный_вариант = models.CharField(max_length = 100, choices = RIGHT_ANSWER_CHOICE,
        default = a_вариант)
    объяснение = models.TextField(null = True, blank = True)
    


    

