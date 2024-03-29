# Generated by Django 3.2 on 2023-02-22 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMatricule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricule', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Client', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('Telephone', models.CharField(blank=True, max_length=8)),
                ('Solde_wallet', models.FloatField()),
                ('CarMatricule', models.ManyToManyField(blank=True, to='clientProfile.CarMatricule')),
            ],
        ),
    ]
