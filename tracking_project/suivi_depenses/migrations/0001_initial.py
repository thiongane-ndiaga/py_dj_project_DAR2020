# Generated by Django 3.0.4 on 2020-03-08 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Suivi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=100)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_limite', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=8)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi_depenses.Categorie')),
                ('suivi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi_depenses.Suivi')),
            ],
        ),
        migrations.AddField(
            model_name='categorie',
            name='suivi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suivi_depenses.Suivi'),
        ),
    ]
