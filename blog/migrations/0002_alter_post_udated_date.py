# Generated by Django 3.2.16 on 2022-12-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='udated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
