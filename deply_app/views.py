from django.shortcuts import render,redirect
from deply_app.models import employee
from django.http import HttpResponse

def show(request):
    data=employee.objects.all()

    print(data)

    return HttpResponse("hello")
from django.http import HttpResponse

def save(request):
    try:
        name = request.POST["name"]
        email = request.POST["email"]

        employee.objects.create(
            name=name,
            email=email
        )

        return HttpResponse("Saved Successfully")

    except Exception as e:
        return HttpResponse(str(e))

def register(request):
    return render(request,"register.html",{})
