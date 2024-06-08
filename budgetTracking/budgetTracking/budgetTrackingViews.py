from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import ast

from budgetTracking import gestionModel, gestionController


def gestion(request):
    activities = gestionModel.getActivities()
    return render(request, 'gestion.html', {'activites': activities})


def add_activity_form(request):
    return render(request, 'addActivityForm.html')

def add_subActivity_form(request):
    idParent = request.GET.get('idParent')
    return render(request, 'addSubActivityForm.html', {'idParent': idParent})

def modify_activity_form(request):
    activite_str = request.GET.get('activite')
    if activite_str:
        activite_list = ast.literal_eval(activite_str)
        context = {
            'id': activite_list[0],
            'idParent': activite_list[1],
            'libelle': activite_list[2],
            'nom': activite_list[3],
            'budget_initial': activite_list[4],
            'budget_depense': activite_list[5],
            'reste': activite_list[6],
            'projection_partielle': activite_list[7],
            'reste_apres_projection': activite_list[8],
            'commentaires': activite_list[9],
        }
    else:
        context = {
            'id': None,
            'idParent': None,
            'libelle': None,
            'nom': None,
            'budget_initial': None,
            'budget_depense': None,
            'reste': None,
            'projection_partielle': None,
            'reste_apres_projection': None,
            'commentaires': None,
        }

    return render(request, 'modifyActivityForm.html', context)

@login_required
def get_new_activity(request):
    if request.method == 'POST':
        return gestionController.saveActivity(request)
    else:
        return HttpResponse('Méthode non autorisée')

@login_required
def modify_activity(request):
    if request.method == 'POST':
        return gestionController.saveActivity(request)
    else:
        return HttpResponse('Méthode non autorisée')


#nv