# Generated by Django 2.0.13 on 2019-10-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0004_auto_20191006_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kualientry',
            name='amount_kuali',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=128, null=True),
        ),
    ]
