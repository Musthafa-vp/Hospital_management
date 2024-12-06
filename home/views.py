from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctors
from .form import BookingForm

# Create your views here.

def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'conformation.html')
    form = BookingForm()
    dict_form = {
        "form":form
    }
    return render(request,"booking.html",dict_form)
def doctors(request):
    dict_doc={
        "doct":Doctors.objects.all()
        }
    return render(request,"docters.html",dict_doc)
def departments(request):
    dict_dept = {
        "dept" : Department.objects.all()
    }
    return render(request,"departments.html",dict_dept)
def contact(request):
    return render(request,"contact.html")
