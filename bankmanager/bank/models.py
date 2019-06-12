from django.db import models

# Create your models here.

class BankDetails(models.Model):
    ifsc_code = models.CharField(max_length=100)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    bank_address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank_name = models.TextField()
