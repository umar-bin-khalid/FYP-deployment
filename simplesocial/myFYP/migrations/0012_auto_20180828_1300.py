# Generated by Django 2.0 on 2018-08-28 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFYP', '0011_auto_20180828_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localities',
            name='location',
            field=models.CharField(choices=[('mustafa town', 'mustafa town'), ('iqbal town', 'iqbal town'), ('johar town', 'johar town'), ('defence', 'defence'), ('defence', 'defence'), ('Awan town', 'Awan town'), ('Eden', 'Eden'), ('Wapda town', 'Wapda town')], default='johar town', max_length=136),
        ),
    ]
