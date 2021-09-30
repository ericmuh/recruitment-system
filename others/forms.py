from django.forms import ModelForm
from .models import Task, Recruitment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class RecruitmentForm(ModelForm):
    class Meta:
        model = Recruitment
        fields = "__all__"

