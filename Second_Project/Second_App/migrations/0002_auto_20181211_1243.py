# Generated by Django 2.1.2 on 2018-12-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Second_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
