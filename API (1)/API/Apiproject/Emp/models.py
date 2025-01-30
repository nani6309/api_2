from django.db import models

# Create your models here.


class Empdetails(models.Model):
    empid = models.BigIntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.BigIntegerField()
    domain = models.CharField( max_length=50)
    mobile = models.BigIntegerField()


    # def __str__(self):
    #     return f'{self.empid} {self.name} {self.age} {self.salary} {self.domain}'