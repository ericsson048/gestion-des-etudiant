from django.urls import path
from app.views import (acceuil, ExporterExcelView,
                       EcarType, EtudiantForm, CoursForm, NoteForm)

urlpatterns = [
    path('', acceuil.as_view(), name='acceuil'),
    path('exporter_excel/', ExporterExcelView.as_view(), name='exporter_excel'),
    path('ecartype/', EcarType, name='detail'),
    path('etudiant/', EtudiantForm.as_view(), name='etudiant'),
    path('cours/', CoursForm.as_view(), name='cours'),
    path('note/', NoteForm.as_view(), name='note'),
]