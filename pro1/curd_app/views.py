from django.shortcuts import render, redirect
from .forms import ExamForm
from .models import Exam
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = ExamForm()
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("register successfully!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Exam.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def updated_view(request, pk):
    template_name = "curd_app/create.html"
    obj = Exam.objects.get(id=pk)
    form = ExamForm()
    if request.method == "POST":
        form = ExamForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Exam.objects.get(id=pk)
    form = ExamForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)

