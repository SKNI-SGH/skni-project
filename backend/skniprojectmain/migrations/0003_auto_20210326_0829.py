# Generated by Django 3.1.5 on 2021-03-26 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skniprojectmain', '0002_auto_20210209_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymeasure',
            name='id_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_companymeasure', to='skniprojectmain.company'),
        ),
    ]