from django.shortcuts import render,redirect
from myapp.models import appodb
# Create your views here.
def index(req):
    return render(req,'index.html')
def blog(req):
    return render(req,'blog.html')
def doc(req):
    return render(req,'doctors.html')
def cont(req):
    return render(req,'contact.html')
def dept(req):
    return render(req,'department.html')
def fake(req):
    return render(req,'fakepage.html')
def ap(req):
    return render(req,'appoinment.html')

def ad(req):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('number')
        c = req.POST.get('date')
        d = req.POST.get('message')
        obj = appodb(Name=a,Number=b,Date=c,Message=d)
        obj.save()
        return redirect(ap)


def addapoo(req):
    if req.method=="POST":
        a = req.POST.get('name')
        b = req.POST.get('number')
        c = req.POST.get('date')
        d = req.POST.get('message')
        obj = appodb(Name=a,Number=b,Date=c,Message=d)
        obj.save()
        return redirect(index)

