# Generated by Django 3.1.7 on 2021-03-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devgarm', '0002_auto_20210329_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
