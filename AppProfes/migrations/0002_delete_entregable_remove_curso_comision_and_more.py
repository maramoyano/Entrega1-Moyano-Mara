# Generated by Django 4.1.3 on 2022-11-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProfes', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='comision',
        ),
        migrations.AddField(
            model_name='curso',
            name='division',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
