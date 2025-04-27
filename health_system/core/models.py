from django.db import models


class HealthProgram(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    full_name=models.CharField(max_length=200)
    age=models.PositiveBigIntegerField()
    contact_number= models.CharField(max_length=20)
    enrolled_programs = models.ManyToManyField(HealthProgram)

    def __str__(self):
        return self.full_name
    

class Enrollment(models.Model):
    client=models.ForeignKey(Client, on_delete=models.CASCADE,related_name='enrollments')
    program=models.ForeignKey(HealthProgram,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_on=models.DateField(auto_now_add=True)


    class Meta:
        unique_together=('client','program')


class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name