from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from finances.models import Fee, Payment, Expense
from finances.forms import FeeForm, PaymentForm, ExpenseForm

# A simple Util Function.
def contextCreater(model, form, form_action ):
    context = {
        # 'a':a,
        'form':form(),
        'form_title': f'{form_action.replace("_", " ").capitalize()}',
        "form_action": form_action,
        "data": model.objects.all()
    }
    return context

@login_required()
def fees(request):
    """
    Fees View

    """
    context = contextCreater(Fee, FeeForm,"add_fees")

    return render(request, 'finances/fees.html', context)

# @login_required()
# def fees(request):
    """
    Fees View
    """
    args = {}
    args['fees'] = Fee.objects.all()
    args['a'] = 'fees'
    return render(request, 'finances/fees.html', args)


# ==================== Add Fee =====================#
@login_required()
def add_fees(request):
    print(request.method)
    if request.method == 'POST':
        form = FeeForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('fees')

    return redirect('fees')
    
@login_required()
def expenses(request):
    """
    Expenses View
    """
    context = contextCreater(Expense, ExpenseForm,"add_expenses")

    return render(request, 'finances/expenses.html', context)




# ==================== Add Expense =====================#
@login_required()
def add_expenses(request):
    print(request.method)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('expense')

    return redirect('expenses')


@login_required()
def payments(request):
    """
    Expenses View
    """
    context = contextCreater(Expense, ExpenseForm,"add_payments")

    return render(request, 'finances/payments.html', context)
# @login_required()
# def payments(request):
#     """
#     Payments View
#     """
#     args = {}
#     args['payments'] = Payment.objects.all()
#     args['a'] = 'payments'
#     return render(request, 'finances/payments.html', args)

# ==================== Add Payment =====================#
@login_required()
def add_payments(request):
    print(request.method)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('payments')

    return redirect('payments')