from django.forms import ModelForm
from .models import Branch

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
