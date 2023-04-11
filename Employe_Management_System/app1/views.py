from django.shortcuts import render,redirect
from .forms import EmployeForms
from .models import Employee
def Home(request):
    form=EmployeForms()
    if request.method=='POST':
        form=EmployeForms(request.POST)
        form.save()
        form=EmployeForms()
    
    data=Employee.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'app1/index.html',context)


def Delete_Record(request,id):
    D_id =Employee.objects.get(pk=id)
    print(D_id.email)
    D_id.delete()
    return redirect('/')

def Update_Record(request,id):
    if request.method=='POST':
        data = Employee.objects.get(pk=id)
        form = EmployeForms(request.POST,instance=data)
        if form.is_valid:
            form.save()
    data = Employee.objects.get(pk=id)
    form = EmployeForms(request.POST,instance=data)
    context = {
        'form': form,
    }
    
    return render(request,'app1/update.html',context)