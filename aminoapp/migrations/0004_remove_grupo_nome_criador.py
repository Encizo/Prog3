# Generated by Django 5.1.4 on 2024-12-15 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aminoapp', '0003_mensagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='nome_criador',
        ),
    ]
