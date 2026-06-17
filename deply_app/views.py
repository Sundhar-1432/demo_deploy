from django.shortcuts import render,redirect
from deply_app.models import employee
from django.http import HttpResponse

def show(request):
    data=employee.objects.all()

    print(data)

    return HttpResponse("hello")
def save(request):
    name=request.POST["name"]
    email=request.POST["email"]

    employee.objects.create(name=name,email=email)

    return redirect('/register')

def register(request):
    return render(request,"register.html",{})
