from django.forms import ModelForm
from .models import Branch, Client, Job

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = "__all__"