from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO = Topicform()
    d = {'ETFO':ETFO}

    if request.method == 'POST':
        TFDO = Topicform(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['topic_name']
            TO = Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Data Inserted into topics')
    return render(request, 'insert_topic.html', d)


def insert_webpage(request):
    EWFO = Webpageform()
    d = {'EWFO' : EWFO}
    if request.method == 'POST':
        WFDO = Webpageform(request.POST)
        if WFDO.is_valid():
            tn = WFDO.cleaned_data['topic_name']
            TO = Topic.objects.get(topic_name=tn)
            n = WFDO.cleaned_data['name']
            u = WFDO.cleaned_data['url']
            e = WFDO.cleaned_data['email']
            WO = Webpage.objects.get_or_create(topic_name=TO, name=n, url=u, email=e)[0]
            WO.save()
            return HttpResponse('Data inserted into webpages')
    return render(request, 'insert_webpage.html', d)


def insert_accessrecord(request):
    EAFO = Accessrecordform()
    d = {'EAFO' : EAFO}
    if request.method == 'POST':
        AFDO = Accessrecordform(request.POST)
        if AFDO.is_valid():
            n = AFDO.cleaned_data['name']
            WO = Webpage.objects.get(pk=n)
            d = AFDO.cleaned_data['date']
            a = AFDO.cleaned_data['author']
            AO = Accessrecord.objects.get_or_create(name=WO, date=d, author=a)[0]
            AO.save()
            return HttpResponse('data inserted into accessrecord')
    return render(request, 'insert_accessrecord.html', d)


def insert_dept(request):
    EDFO = Deptform()
    d = {'EDFO' : EDFO}
    if request.method == 'POST':
        DDFO = Deptform(request.POST)
        if DDFO.is_valid():
            dno = DDFO.cleaned_data['deptno']
            dn = DDFO.cleaned_data['dname']
            dl = DDFO.cleaned_data['dloc']
            DO = Dept.objects.get_or_create(deptno=dno, dname=dn, dloc=dl)[0]
            DO.save()
            return HttpResponse('Data inserted into dept')
    return render(request, 'insert_dept.html', d)

def insert_emp(request):
    EEFO = Empform()
    d = {'EEFO' : EEFO}
    if request.method == 'POST':
        EDFO = Empform(request.POST)
        if EDFO.is_valid():
            dno = EDFO.cleaned_data['deptno']
            eid = EDFO.cleaned_data['eid']
            ename = EDFO.cleaned_data['ename']
            sal = EDFO.cleaned_data['sal']
            DO = Dept.objects.get(deptno=dno)
            EO = Emp.objects.get_or_create(eid=eid, ename=ename, sal=sal, deptno=DO)[0]
            EO.save()
            return HttpResponse('Data inserted into employee')
    return render(request, 'insert_emp.html', d)

