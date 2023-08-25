# Generated by Django 4.2.4 on 2023-08-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Importer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("importer_name", models.CharField(max_length=50)),
                ("address", models.TextField(max_length=100)),
                ("license_number", models.IntegerField()),
                ("lic_date", models.DateField()),
                ("bond_number", models.IntegerField()),
                ("gmail_id", models.EmailField(max_length=254)),
                (
                    "radio_choice",
                    models.CharField(
                        choices=[("EPCG", "EPCG"), ("DECC", "DECC")], max_length=4
                    ),
                ),
                ("is_eodc_produced", models.BooleanField(default=False)),
                ("is_dgft_ack_produced", models.BooleanField(default=False)),
                ("is_letter_issued", models.BooleanField(default=False)),
                ("is_scn_issued", models.BooleanField(default=False)),
                ("is_ph1_issued", models.BooleanField(default=False)),
                ("is_ph2_issued", models.BooleanField(default=False)),
                ("is_oio_issued", models.BooleanField(default=False)),
            ],
        ),
    ]
