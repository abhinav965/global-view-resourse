from django.db import models

# Create your models here.



class appodb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Number=models.IntegerField(max_length=100,null=True,blank=True)
    Date=models.DateField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)