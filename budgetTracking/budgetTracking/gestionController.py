from django.http import HttpResponse
from django.shortcuts import redirect

from budgetTracking import gestionModel

def saveActivity(request):
    id = request.POST['id']
    idParent = request.POST['idParent']
    libelle = request.POST['libelle']
    nom = request.POST['nom']
    budget_initial = request.POST['budget_initial']
    budget_depense = request.POST['budget_depense']
    reste = request.POST['budget_initial']
    projection_partielle = request.POST['projection_partielle']
    reste_apres_projection = int(request.POST['budget_initial']) - int(request.POST['projection_partielle'])
    commentaires = request.POST['commentaires']

    if id == "":
        gestionModel.saveActivityToBDD(idParent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection, commentaires)

    else :
        gestionModel.updateActivity(id, idParent, libelle, nom, budget_initial, budget_depense, reste, projection_partielle, reste_apres_projection, commentaires)

    if idParent != "0":
        updateBudgetDepense(idParent)
        updateReste(idParent)
    
      # Créez le message que vous voulez afficher dans la console
    message = (f'Données reçues : \n'
               f'idParent : {idParent}\n'
               f'Libellé : {libelle}\n'
               f'Nom : {nom}\n'
               f'Budget Initial : {budget_initial}\n'
               f'Budget Dépensé : {budget_depense}\n'
               f'Reste : {reste}\n'
               f'Projection Partielle : {projection_partielle}\n'
               f'Reste après Projection : {reste_apres_projection}\n'
               f'Commentaires : {commentaires}')
    
    # Imprimez le message dans la console
    print(message)

    return redirect('/gestion')

def updateBudgetDepense(id):
    activity = gestionModel.getActivityById(id)
    subActivities = gestionModel.getSubActivitiesByIdParent(id)
    budgetDepense = 0
    for subActivity in subActivities : 
        budgetDepense += subActivity[4]
        print(budgetDepense)
    gestionModel.updateBudgetDepense(id, budgetDepense)

def updateReste(id):
    if(id != "0"):
        activity = gestionModel.getActivityById(id)
        reste = int(activity[0][4]) - int(activity[0][5])
        gestionModel.updateReste(id, reste)
