# Generated by Django 3.0.6 on 2020-06-10 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20200610_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='картинка',
            field=models.ImageField(blank=True, null=True, upload_to='questionImages'),
        ),
    ]
