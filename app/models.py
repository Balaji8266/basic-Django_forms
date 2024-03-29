from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name 

class Accessrecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    dloc = models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Emp(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    sal = models.IntegerField()
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.ename 



