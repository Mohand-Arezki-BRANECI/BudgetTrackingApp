from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from budgetTracking import gestionController, gestionModel

@login_required
def gestion(request):
    activities = gestionModel.getActivities()
    sub_activities = gestionModel.getSubActivities()
    return render(request, 'gestion.html', {'activites': activities, 'sub_activites': sub_activities})


@login_required
def add_activity_form(request):
    return render(request, 'addActivityForm.html')

@login_required
def add_subActivity_form(request):
    idParent = request.GET.get('idParent')
    return render(request, 'addSubActivityForm.html', {'idParent': idParent})

@login_required
def get_new_activity(request):
    if request.method == 'POST':
        return gestionController.saveActivity(request)
    else:
        return HttpResponse('Méthode non autorisée')