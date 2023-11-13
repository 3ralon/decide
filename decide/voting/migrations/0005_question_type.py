# Generated by Django 4.1 on 2023-11-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_alter_voting_postproc_alter_voting_tally'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('DEFAULT', 'Default'), ('YESNO', 'Yes/No'), ('MULTIPLE_CHOICE', 'Multiple Choice')], default='DEFAULT', max_length=20),
        ),
    ]
