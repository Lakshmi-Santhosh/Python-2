# Generated by Django 4.2.4 on 2023-08-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name1',
            field=models.CharField(max_length=100),
        ),
    ]
