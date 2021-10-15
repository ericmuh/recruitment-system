from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from others.models import Task, Recruitment
from others.forms import TaskForm, RecruitmentForm


# A simple Util Function.
def contextCreater(model, form, form_action, a="a"):
    context = {
        'pending': model.objects.filter(status=0).count(),
        'active': model.objects.filter(status=1).count(),
        'done': model.objects.filter(status=2).count(),
        'cancelled': model.objects.filter(status=3).count(),
        'passed': model.objects.filter(status=4).count(),
        'failed': model.objects.filter(status=5).count(),
        'form':form(),
        'form_title': f'{form_action.replace("_", " ").capitalize()}',
        "form_action": form_action,
        "data": model.objects.all(),
        "a":a
    }
    return context

@login_required()
def tasks(request):
    """
    tasks View
    """
    context = contextCreater(Task, TaskForm,"add_task", a="tasks")

    return render(request, 'others/tasks.html', context)

    

@login_required()
def add_task(request):
    print(request.method)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('tasks')
    return redirect('tasks')

@login_required()
def recruitments(request):
    """
    recruitments View
    """
    context = contextCreater(Recruitment, RecruitmentForm,"add_recruitment",a="recruitments")

    return render(request, 'others/recruitments.html', context)




@login_required()
def add_recruitment(request):
    print(request.method)
    if request.method == 'POST':
        form = RecruitmentForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('recruitments')
    return redirect('recruitments')