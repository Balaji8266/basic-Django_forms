from django import forms
from app.models import *

class Topicform(forms.Form):
    topic_name = forms.CharField()


class Webpageform(forms.Form):
    topic_list = [[to.topic_name, to.topic_name] for to in Topic.objects.all()]
    topic_name = forms.ChoiceField(choices=topic_list)
    name = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField()


class Accessrecordform(forms.Form):
    Webpage_list = [[wo.pk, wo.name] for wo in Webpage.objects.all()]
    name = forms.ChoiceField(choices=Webpage_list)
    date = forms.DateField()
    author = forms.CharField()

class Deptform(forms.Form):
    deptno = forms.IntegerField()
    dname = forms.CharField()
    dloc = forms.CharField()


class Empform(forms.Form):
    dept_list = [[do.deptno, do.deptno] for do in Dept.objects.all()]
    deptno = forms.ChoiceField(choices=dept_list)
    eid = forms.IntegerField()
    ename = forms.CharField()
    sal = forms.IntegerField()
    
    