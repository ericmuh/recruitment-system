from django.urls import path
from . import views

from files import views as files
from finances import views as finances
from others import views as others
from operations import views as operations

urlpatterns = [

    path('clients/<int:client_id>/pay-reg-fee',
         views.pay_reg_fee, name='pay-reg-fee'),
    path('clients/<int:client_id>/register', views.register, name='register'),

    path('clients', views.clients, name='clients'),
    path('jobs', views.jobs, name='jobs'),
    path('branches', views.branches, name='branches'),
    path('add_branch/', views.add_branch, name='add_branch'),

    # operations
    path('clearances', operations.clearances, name='clearances'),
    path('contracts', operations.contracts, name='contracts'),
    path('interpols', operations.interpols, name='interpols'),
    path('interviews', operations.interviews, name='interviews'),

    # ======== post routes===============#
    path('add-interview/', operations.add_interview, name='add-interview'),
    path('add_clearance/', operations.add_clearance, name='add_clearance'),
    path('add_contract/', operations.add_contract, name='add_contract'),
    path('add_training/', operations.add_training, name='add_training'),
    path('add_medical/', operations.add_medical, name='add_medical'),
    path('add_passport/', operations.add_passport, name='add_passport'),
    path('add_ticket/', operations.add_ticket, name='add_ticket'),
    path('add_visa/', operations.add_visa, name='add_visa'),
    path('add_other_operation/', operations.add_other_operation, name='add_other_operation'),
    path('add_travel_plan/', operations.add_travel_plan, name='add_travel_plan'),
    path('add_vetting/', operations.add_vetting, name='add_vetting'),
    path('add_vetting_ablum/', operations.add_vetting_ablum, name='add_vetting_ablum'),



    path('trainings', operations.trainings, name='trainings'),
    path('medicals', operations.medicals, name='medicals'),
    path('passports', operations.passports, name='passports'),
    path('tickets', operations.tickets, name='tickets'),
    path('vettings', operations.vettings, name='vettings'),
    path('vetting-album', operations.vetting_album, name='vetting-album'),
    path('visas', operations.visas, name='visas'),
    path('travel-plans', operations.travel_plans, name='travel-plans'),
    path('other-ops', operations.other_ops, name='other-ops'),

    # finances
    path('payments', finances.payments, name='payments'),
    path('expenses', finances.expenses, name='expenses'),
    path('fees', finances.fees, name='fees'),
    path('add_fees/', finances.add_fees, name='add_fees'),

    # files
    path('clearance-files', files.clearance_files, name='clearance-files'),
    path('client-files', files.client_files, name='client-files'),

    # others
    path('tasks', others.tasks, name='tasks'),
    path('recruitments', others.recruitments, name='recruitments'),

    path('', views.index, name="index"),
]
