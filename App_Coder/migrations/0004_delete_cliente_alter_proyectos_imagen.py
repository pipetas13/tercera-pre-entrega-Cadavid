# Generated by Django 4.1.5 on 2023-02-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Coder', '0003_proyectos_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cliente',
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='NFTs'),
        ),
    ]
