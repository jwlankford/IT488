from django.db import models

class OrderData(models.Model):
   firstname = models.CharField(max_length=200)
   cases = models.CharField(max_length=200)

   def __str__(self):
       return f'{self.firstname} : {self.cases}'
