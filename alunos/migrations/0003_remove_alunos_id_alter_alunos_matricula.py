# Generated by Django 4.2.1 on 2023-06-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_alter_alunos_matricula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alunos',
            name='id',
        ),
        migrations.AlterField(
            model_name='alunos',
            name='matricula',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
