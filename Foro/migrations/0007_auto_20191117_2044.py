# Generated by Django 2.2.6 on 2019-11-17 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Foro', '0006_auto_20191117_2040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('user', 'Es Admin'), ('usuraio', 'Es Usuraio'))},
        ),
    ]
