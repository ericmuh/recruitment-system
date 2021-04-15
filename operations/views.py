from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from operations.models import Clearance, Contract, Interpol, Interview, Medical, Passport, Ticket, Vetting, Visa, OtherOperation, Training, Travel
from .forms import InterviewForm, ClearanceForm,ContractForm, TravelForm, TrainingForm,VisaForm, VettingForm, OtherOperationForm, TicketForm,MedicalForm, InterpolForm, PassportForm


# A simple Util Function.
def contextCreater(model, form, form_action):
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
        "data": model.objects.all()
    }
    return context


# ////////////////////////////////////////////////
# ClEARANCES
# ////////////////////////////////////////////////
@login_required()
def clearances(request):
    """
    Clearances View
    """
    context = contextCreater(Clearance, ClearanceForm,"add_clearance")

    return render(request, 'operations/clearances.html', context)


# ==================== Add Clearance =====================#
@login_required()
def add_clearance(request):
    print(request.method)
    if request.method == 'POST':
        form = ClearanceForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
    return redirect('clearances')


# ////////////////////////////////////////////////
# CONTRACTS
# ////////////////////////////////////////////////
@login_required()
def contracts(request):
    """
    Contracts View
    """
    context = contextCreater(Contract, ContractForm,"add_contract")
    return render(request, 'operations/contracts.html', context)
# ==================== Add Contract =====================#
@login_required()
def add_contract(request):
    print(request.method)
    if request.method == 'POST':
        form = ContractForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('contracts')

    return redirect('contracts')

# ////////////////////////////////////////////////
# CONTRACTS
# ////////////////////////////////////////////////
@login_required()
def interpols(request):
    """
    Interpols View
    """
    context = contextCreater(Interpol, InterpolForm,"add_interpol")
    return render(request, 'operations/interpols.html', context)

@login_required()
def add_interpol(request):
    print(request.method)
    if request.method == 'POST':
        form = InterpolForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('interpols')
    return redirect('interpols')


# ////////////////////////////////////////////////
# INTERVIEWS
# ////////////////////////////////////////////////
@login_required()
def interviews(request):
    """
    Interviews View
    """
    context = contextCreater(Interview, InterviewForm,"add_interview")
    return render(request, 'operations/interviews.html', context)

# ==================== Add interviews Form =====================#


@login_required()
def add_interview(request):
    print(request.method)
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('interviews')
    return redirect('interviews')


# ////////////////////////////////////////////////
# TRAININGS
# ////////////////////////////////////////////////
@login_required()
def trainings(request):
    """
    Trainings View
    """
    context = contextCreater(Training, TrainingForm,"add_training")
    return render(request, 'operations/trainings.html', context)

@login_required()
def add_training(request):
    print(request.method)
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('traininigs')
    return redirect('trainings')

# ////////////////////////////////////////////////
# MEDICALS
# ////////////////////////////////////////////////
@login_required()
def medicals(request):
    """
    Medicals View
    """
    context = contextCreater(Medical, MedicalForm,"add_medical")
    return render(request, 'operations/medicals.html', context)

@login_required()
def add_medical(request):
    print(request.method)
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('medicals')
    return redirect('medicals')

# ////////////////////////////////////////////////
# OTHER OPERATIONS
# ////////////////////////////////////////////////
@login_required()
def other_ops(request):
    """
    Other Operations View
    """
    context = contextCreater(OtherOperation, OtherOperationForm,"add_other_operation")
    return render(request, 'operations/other-ops.html', context)

@login_required()
def add_other_operation(request):
    print(request.method)
    if request.method == 'POST':
        form = OtherOperationForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('other_ops')
    return redirect('other_ops')

# ////////////////////////////////////////////////
# PASSPORTS
# ////////////////////////////////////////////////
@login_required()
def passports(request):
    """
    Passports View
    """
    context = contextCreater(Passport, PassportForm,"add_passport")
    return render(request, 'operations/passports.html', context)

@login_required()
def add_passport(request):
    print(request.method)
    if request.method == 'POST':
        form = PassportForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('passports')
    return redirect('passports')

# ////////////////////////////////////////////////
# TICKETS
# ////////////////////////////////////////////////
@login_required()
def tickets(request):
    """
    Tickets View
    """
    context = contextCreater(Ticket,TicketForm,"add_ticket")
    return render(request, 'operations/tickets.html', context)

@login_required()
def add_ticket(request):
    print(request.method)
    if request.method == 'POST':
        form = OtherOperationForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('tickets')
    return redirect('tickets')
# ////////////////////////////////////////////////
# VETTINGS
# ////////////////////////////////////////////////


@login_required()
def vettings(request):
    """
    Vettings View
    """
    context = contextCreater(Vetting, VettingForm, "add_vetting")
    return render(request, 'operations/vetting/list.html', context)

@login_required()
def add_vetting(request):
    print(request.method)
    if request.method == 'POST':
        form = VettingForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('vettings')
    return redirect('vettings')

@login_required()
def vetting_album(request):
    """
    Vetting Album View
    """
    context = contextCreater(Vetting, VettingForm,"add_vetting")
    return render(request, 'operations/vetting/album.html', context)


@login_required()
def add_vetting_ablum(request):
    print(request.method)
    if request.method == 'POST':
        form = VettingAlbumForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('vetting_album')
    return redirect('vetting_album')

# ////////////////////////////////////////////////
# VISAS
# ////////////////////////////////////////////////
@login_required()
def visas(request):
    """
    Visas View
    """
    context = contextCreater(Visa,VisaForm,"add_visa")

    return render(request, 'operations/visas.html', context)

@login_required()
def add_visa(request):
    print(request.method)
    if request.method == 'POST':
        form = VisaForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('visa')
    return redirect('visa')
# ////////////////////////////////////////////////
# TRAVELS
# ////////////////////////////////////////////////
@login_required()
def travel_plans(request):
    """
    Travel Plans View
    """
    context = contextCreater(Travel, TravelForm,"add_travel_plan")

    return render(request, 'operations/travel-plans.html', context)


@login_required()
def add_travel_plan(request):
    print(request.method)
    if request.method == 'POST':
        form = TravelForm(request.POST)
        print(form.data)
        print(form.errors)
        print(form.is_valid(), "🤞")
        if form.is_valid():
            print("everything is 👌")
            form.save()
            return redirect('travel_plans')
    return redirect('travel_plans')