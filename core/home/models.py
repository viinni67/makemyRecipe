from django.db import models

# Create your models here.

class students(models.Model):
    # S_no=models.AutoField()
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=False,blank=False)
    email=models.EmailField(null=False)
    address=models.TextField(max_length=2000)
    # image=models.ImageField()

class bikes(models.Model):
    b_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=100)
    mileage=models.IntegerField()

    def __str__(self) -> str:
        return self.b_name
