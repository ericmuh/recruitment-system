from django.forms import ModelForm
from operations.models import Clearance, Contract, Interpol, Interview, Medical, Passport, Ticket, Vetting, Visa, OtherOperation, Training, Travel

# Create the form class.

ModelList = [Clearance, Contract, Interpol, Interview, Medical,
            Passport, Ticket, Vetting, Visa, OtherOperation, Training, Travel]


# for model in ModelForm:
#     class f''

class ClearanceForm(ModelForm):
    class Meta:
        model = Clearance
        fields = "__all__"


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"


class InterpolForm(ModelForm):
    class Meta:
        model = Interpol
        fields = "__all__"


class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = "__all__"


class MedicalForm(ModelForm):
    class Meta:
        model = Medical
        fields = "__all__"


class PassportForm(ModelForm):
    class Meta:
        model = Passport
        fields = "__all__"


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"


class VettingForm(ModelForm):
    class Meta:
        model = Vetting
        fields = "__all__"


class VisaForm(ModelForm):
    class Meta:
        model = Visa
        fields = "__all__"


class OtherOperationForm(ModelForm):
    class Meta:
        model = OtherOperation
        fields = "__all__"


class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = "__all__"


class TravelForm(ModelForm):
    class Meta:
        model = OtherOperation
        fields = "__all__"
