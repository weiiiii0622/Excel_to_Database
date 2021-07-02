from django.db import models

# Create your models here.

GENDER = [
	('男', '男'),
	('女', '女'),
]

GRADE = [
    ('小3', '小3'),
    ('小4', '小4'),
    ('小5', '小5'),
    ('小6', '小6'),
]

class Lesson(models.Model):
    name = models.TextField(unique=True)
    limit = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=256, choices=GENDER)
    school = models.CharField(max_length=256)
    grade = models.CharField(max_length=256, choices=GRADE)
    lesson_selected = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True)
    lesson_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Info(models.Model):
    name = models.ForeignKey('User', on_delete=models.CASCADE)
    gender = models.CharField(max_length=256, choices=GENDER)
    school = models.CharField(max_length=256)
    grade = models.CharField(max_length=256, choices=GRADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name













