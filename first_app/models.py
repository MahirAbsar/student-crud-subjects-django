from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Subject(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    difficulty = (
    (1,"Very Easy"),
    (2,"Easy"),
    (3,"Medium"),
    (4,"Hard"),
    (4,"DROPPP!!!!!"),
    )
    difficulty_level = models.IntegerField(choices=difficulty)

    def __str__(self):
        return self.name+" Difficulty Level: "+str(self.difficulty_level)
