# Generated by Django 3.0.6 on 2020-06-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_explanation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='fifth_choice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='first_choice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='fourth_choice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='right_choice',
            field=models.CharField(choices=[('first_choice', 'FIRST_CHOICE'), ('second_choice', 'SECOND_CHOICE'), ('third_choice', 'THIRD_CHOICE'), ('fourth_choice', 'FOURTH_CHOICE'), ('fifth_choice', 'FIFTH_CHOICE')], default=models.CharField(max_length=100, null=True), max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='second_choice',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='third_choice',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
