import statistics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from app.models import Note, Etudiant, Cours
from django.http import HttpResponse
from django.views import View
import pandas as pd
from .forms import EtudiantForm
import numpy as np
from django.db.models import Q, StdDev


class acceuil(ListView):
    model = Note
    context_object_name = 'form'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(
                Q(note__icontains=q) |
                Q(etudiant__NomEtudiant__icontains=q) |
                Q(etudiant__PrenomEtudiant__icontains=q) |
                Q(cours__NomCours__icontains=q) |
                Q(etudiant__Matricule__icontains=q)
            )
        return queryset


def EcarType(request):
    etudiants = Etudiant.objects.all()
    selected_etudiant = None
    if request.method == 'POST':
        selected_etudiant = Etudiant.objects.get(
            CodeEtudiant=request.POST['etudiant'])
        notes = selected_etudiant.note_set.all().values_list('note', flat=True)
        if len(notes) > 1:
            selected_etudiant.ecart_type = statistics.stdev(notes)
        else:
            selected_etudiant.ecart_type = 0
    return render(request, 'detail.html', {'etudiants': etudiants, 'selected_etudiant': selected_etudiant})


class ExporterExcelView(View):
    def get(self, request, *args, **kwargs):
        # Récupérer les données de la base de données
        queryset = Note.objects.select_related('etudiant', 'cours').all()

        # Convertir le queryset en une liste de dictionnaires
        data = queryset.values('CodeNote', 'etudiant__NomEtudiant', 'etudiant__PrenomEtudiant',
                               'cours__NomCours', 'cours__Volume', 'note', 'createdOn')

        # Convertir la liste de dictionnaires en un DataFrame pandas
        df = pd.DataFrame.from_records(data)

        # Rendre les objets datetime indépendants du fuseau horaire
        df['createdOn'] = df['createdOn'].dt.tz_convert(None)

        # Créer une réponse HTTP avec un type de contenu Excel
        response = HttpResponse(content_type='application/vnd.ms-excel')

        # Créer un nom de fichier
        response['Content-Disposition'] = 'attachment; filename=Note2.xlsx'

        # Écrire le DataFrame dans la réponse HTTP
        df.to_excel(response, index=False)

        return response


class EtudiantForm(CreateView):
    model = Etudiant
    fields = "__all__"
    context_object_name = 'form'
    template_name = 'etudiant.html'
    success_url = reverse_lazy('acceuil')


class CoursForm(CreateView):
    model = Cours
    fields = "__all__"
    context_object_name = 'form'
    template_name = 'cours.html'
    success_url = reverse_lazy('acceuil')


class NoteForm(CreateView):
    model = Note
    fields = "__all__"
    context_object_name = 'form'
    template_name = 'note.html'
    success_url = reverse_lazy('acceuil')
