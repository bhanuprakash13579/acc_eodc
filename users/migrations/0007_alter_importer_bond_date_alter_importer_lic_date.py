# Generated by Django 4.2.4 on 2023-08-31 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_importer_bond_date_alter_importer_lic_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="importer",
            name="bond_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 31, 9, 8, 18, 210707, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="importer",
            name="lic_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 31, 9, 8, 18, 209323, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
