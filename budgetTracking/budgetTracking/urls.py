# urls.py
from django.contrib import admin
from django.urls import path, include
from google_authentication import views
from budgetTracking import budgetTrackingViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
    path('gestion/', budgetTrackingViews.gestion, name='gestion'),
    path('add_activity_form/', budgetTrackingViews.add_activity_form, name='add_activity_form'),
    path('add_subActivity_form/', budgetTrackingViews.add_subActivity_form, name='add_subActivity_form'),
    path('modify_activity_form/', budgetTrackingViews.modify_activity_form, name='modify_activity_form'),
    path('get_new_activity/', budgetTrackingViews.get_new_activity, name='get_new_activity'),
    path('modify_activity/', budgetTrackingViews.modify_activity, name='modify_activity'),
]
