from django.contrib import messages
from django.shortcuts import render, redirect

from newapp.forms import taskform,detailform
from newapp.models import task,details


# Create your views here.
def First(request):
    form = taskform()
    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("First")
    return render(request,"first.html", {"form": form})

#
def task_view(request):
    data = task.objects.all()

    return render(request,"taskview.html",{"data":data})

def delete(request,id):
    if request.method =='POST':
        task .objects.get(id=id).delete()
        messages.info(request, "deleted")
        return redirect("task_view")


def admin1(request):
    return render(request,"admin.html")



def dtails(request):
    form = detailform()
    if request.method == "POST":
        form = detailform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("First")
    return render(request,"DETAILS.html", {"form": form} )



def detailsview(request):
    data = details.objects.all()
    return render(request, "detailsview.html", {"data": data})

def TaskUpdate(request,id):
    data = task.objects.get(id=id)
    form = taskform(instance=data)
    if request.method == 'POST':
        form = taskform(request.POST, instance=data)
        if form.is_valid():
            form.save()
        return redirect("task_view")
    return render(request,"taskupdate.html", {'form': form})


def count(request):
    count = task.objects.all().count()
    context = {'count': count}
    return render(request,"count.html",context)
