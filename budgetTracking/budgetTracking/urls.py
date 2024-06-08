"""
URL configuration for budgetTracking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from google_authentication import views
from budgetTracking import budgetTrackingViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
    path('gestion/', budgetTrackingViews.gestion, name='gestion'),
    path('add_activity_form/', budgetTrackingViews.add_activity_form, name='add_activity_form'),
    path('add_subActivity_form/', budgetTrackingViews.add_subActivity_form, name='add_subActivity_form'),
    path('modify_activity_form/', budgetTrackingViews.modify_activity_form, name='modify_activity_form'),
    path('get_new_activity/', budgetTrackingViews.get_new_activity, name='get_new_activity'),
    path('modify_activity/', budgetTrackingViews.modify_activity, name='modify_activity'),
]