# Generated by Django 5.0 on 2024-02-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_note_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]