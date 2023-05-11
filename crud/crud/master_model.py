from django.db import models
class DetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    school=models.CharField(max_length=100)
    grade=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    def __str__(self):
        return self.name or ''