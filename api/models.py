from django.db import models

# Create your models here.
class bank(models.Model):
    
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name

    
class branch(models.Model):
    
    ifsc = models.CharField( max_length=11, primary_key=True)
    bank_id = models.ForeignKey(bank,  on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField( max_length=195)

    city = models.CharField( max_length=50)
    district = models.CharField( max_length=50)
    state = models.CharField( max_length=26)

    def __str__(self):
        return self.ifsc

    