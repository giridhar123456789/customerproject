from django.db import models

class customer(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=10)
    cjob=models.CharField(max_length=20)
    cbranch=models.CharField(max_length=30)
    cbalance=models.DecimalField(max_digits=10,decimal_places=2)
