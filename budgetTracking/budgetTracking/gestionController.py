from django.http import HttpResponse
from django.shortcuts import redirect


from budgetTracking import gestionModel

def saveActivity(request):
    idParent = request.POST['idParent']
    libelle = request.POST['libelle']
    nom = request.POST['nom']
    budget_initial = request.POST['budget_initial']
    budget_depense = request.POST['budget_depense']
    reste = request.POST['reste']
    projection_partielle = request.POST['projection_partielle']
    reste_apres_projection = request.POST['reste_apres_projection']
    commentaires = request.POST['commentaires']

    gestionModel.saveActivityToBDD(idParent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection, commentaires)

    return HttpResponse(f'Données reçues : <br>idParent : {idParent}<br>Libellé : {libelle}<br>Nom : {nom}<br>Budget Initial : {budget_initial}<br>Budget Dépensé : {budget_depense}<br>Reste : {reste}<br>Projection Partielle : {projection_partielle}<br>Reste après Projection : {reste_apres_projection}<br>Commentaires : {commentaires}')

def calculBudgetDepense(idActivity):
    subActivities = gestionModel.getSubActivitiesByIdParent(idActivity)
    budgetDepense = 0
    for activite in subActivities:
        budgetDepense += activite[5]
    return budgetDepense

def calculReste(idActivity):
    activite = gestionModel.getActivityById(idActivity)
    budgetInitial = activite[4]
    budetDepense = activite[5]
    reste = budgetInitial - budetDepense
    return reste


