"""
URL configuration for projet project.

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
import allauth
from django.contrib import admin
from django.urls import path, include
from app.views import (acceuil, ExporterExcelView,
                       EcarType, EtudiantForm, CoursForm, NoteForm)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', acceuil.as_view(), name='acceuil'),
    path('exporter_excel/', ExporterExcelView.as_view(), name='exporter_excel'),
    path('ecartype/', EcarType, name='detail'),
    path('etudiant/', EtudiantForm.as_view(), name='etudiant'),
    path('cours/', CoursForm.as_view(), name='cours'),
    path('note/', NoteForm.as_view(), name='note'),
]

