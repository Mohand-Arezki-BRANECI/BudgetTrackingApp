from django.http import HttpResponse

from budgetTracking import gestionModel

def saveActivity(request):
    id = request.POST['id']
    id_parent = request.POST['id_parent']
    libelle = request.POST['libelle']
    nom = request.POST['nom']
    budget_initial = request.POST['budget_initial']
    budget_depense = 0
    reste = request.POST['budget_initial']
    projection_partielle = request.POST['projection_partielle']
    reste_apres_projection = int(request.POST['budget_initial']) - int(request.POST['projection_partielle'])
    commentaires = request.POST['commentaires']

    if id == "":
        gestionModel.saveActivityToBDD(id_parent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection, commentaires)

    else :
        gestionModel.updateActivity(id, id_parent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection, commentaires)

    if id_parent != "0":
        updateBudgetDepense(id_parent, budget_initial)
        updateReste(id_parent, budget_initial)

    return HttpResponse(f'Données reçues : <br>idParent : {id_parent}<br>Libellé : {libelle}<br>Nom : {nom}<br>Budget Initial : {budget_initial}<br>Budget Dépensé : {budget_depense}<br>Reste : {reste}<br>Projection Partielle : {projection_partielle}<br>Reste après Projection : {reste_apres_projection}<br>Commentaires : {commentaires}')

def updateBudgetDepense(id, budget_initial):
    activity = gestionModel.getActivityById(id)
    budgetDepense = int(activity[0][5]) + int(budget_initial)
    gestionModel.updateBudgetDepense(id, budgetDepense)

def updateReste(id, budget_initial):
    if(id != "0"):
        activity = gestionModel.getActivityById(id)
        reste = int(activity[0][6]) - int(budget_initial)
        gestionModel.updateReste(id, reste)





