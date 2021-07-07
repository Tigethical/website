from django.db import models

# Create your models here.
class skills(models.Model):
    skill=models.CharField(max_length=100)
    percentage=models.IntegerField()

class overview(models.Model):
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    badge=models.CharField(max_length=100)

class Education(models.Model):
    degree=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    dec=models.TextField()
    date=models.CharField(max_length=100)

class Acheivements(models.Model):
    name=models.CharField(max_length=100)
    dec_name=models.CharField(max_length=100)
    dec=models.TextField()
    status=models.CharField(max_length=100)


class certifications(models.Model):
    name=models.CharField(max_length=100)
    dec=models.TextField()
    date=models.CharField(max_length=100)
    Images=models.ImageField(upload_to='pics')
    number=models.IntegerField()

class projects(models.Model):
    name=models.CharField(max_length=100)
    dec=models.TextField()
    Images=models.ImageField(upload_to='pics')

class FilesAdmin(models.Model):
    adminupload=models.FileField(upload_to='pics')