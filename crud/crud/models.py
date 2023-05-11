from django.db import models
class DetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    school=models.CharField(max_length=100, null=True)
    grade=models.CharField(max_length=100, null=True)
    city=models.CharField(max_length=100, null=True)
    branch=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.name or ''