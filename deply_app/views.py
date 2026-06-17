from django.shortcuts import render,redirect
from deply_app.models import employee,Contact
from django.http import HttpResponse


def store(request):
    name=request.POST['name']
    email=request.POST['email']
    subject=request.POST['subject']
    message=request.POST['message']

    Contact.objects.create(name=name,email=email,subject=subject,message=message)

    return HttpResponse("data stored successfully")


def contact(request):
    return render(request,"contact.html",{})
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
