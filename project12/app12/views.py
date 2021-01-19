from django.shortcuts import render
from .models import Employeemodel
from django.http import Http404

def showIndex(request):
    employee = Employeemodel.objects.all()
    return render(request,"home.html",{'employee':employee})


def emp_details(request,employee_id):
    try:
        employee = Employeemodel.objects.get(id=employee_id)
    except Employeemodel.DoesNotExist:
        raise Http404('Employee Not Exists')
    return render(request,'details.html',{'employee':employee})