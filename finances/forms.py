from django.forms import ModelForm

from finances.models import Fee, Payment, Expense

# Create the form class.

ModelList = [Fee, Payment, Expense]


# for model in ModelForm:
#     class f''

class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = "__all__"


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"
