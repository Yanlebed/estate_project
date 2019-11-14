# Generated by Django 2.1.1 on 2019-11-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
