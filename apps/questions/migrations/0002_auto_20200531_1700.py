# Generated by Django 3.0.6 on 2020-05-31 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='introduction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='questions.Introduction'),
        ),
    ]
