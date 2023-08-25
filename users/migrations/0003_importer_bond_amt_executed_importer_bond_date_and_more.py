# Generated by Django 4.2.4 on 2023-08-23 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_importer_lic_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="importer",
            name="bond_amt_executed",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="importer",
            name="bond_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 23, 16, 59, 21, 883882, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AddField(
            model_name="importer",
            name="duty_saved",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="importer",
            name="iec_code",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="importer",
            name="items_imported",
            field=models.CharField(default="machines", max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="importer",
            name="lic_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 23, 16, 59, 21, 883882, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
