# Generated by Django 3.0.6 on 2020-06-16 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_tasks'),
        ('questions', '0015_auto_20200616_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='пользователь',
        ),
        migrations.AddField(
            model_name='review',
            name='профайл',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ответы',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Answer'),
        ),
    ]
