from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    mark = models.IntegerField()

    def __str__(self):
        return self.name

# class Subcriber(models.Model):
#     s_email = models.EmailField(max_length=200)

#     def __str__(self):  
#         return self.sub_email

class Subcriber(models.Model):
    s_email = models.EmailField(max_length=200)

    def __str__(self):
        return self.s_email


class Mobilephone(models.Model):
    spmodel = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    RAM = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.brand + ' '+ self.spmodel