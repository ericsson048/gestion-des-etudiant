# Generated by Django 5.0.2 on 2024-02-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='createdOn',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddConstraint(
            model_name='note',
            constraint=models.UniqueConstraint(fields=('etudiant', 'cours'), name='unique_etudiant_cours'),
        ),
    ]