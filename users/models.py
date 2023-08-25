from django.db import models
from django.utils import timezone


class Importer(models.Model):
    CHOICES = [('EPCG', 'EPCG'), ('DECC', 'DECC')]
    importer_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    license_number = models.IntegerField()
    lic_date = models.DateField(default=timezone.now())
    bond_number = models.IntegerField()
    gmail_id = models.EmailField()
    radio_choice = models.CharField(max_length=4, choices=CHOICES)

    iec_code = models.IntegerField()
    items_imported = models.CharField(max_length=150)
    duty_saved = models.IntegerField()
    bond_amt_executed = models.IntegerField()
    bond_date = models.DateField(default=timezone.now())


    # Boolean fields
    is_eodc_produced = models.BooleanField(default=False)
    is_dgft_ack_produced = models.BooleanField(default=False)
    is_letter_issued = models.BooleanField(default=False)
    is_scn_issued = models.BooleanField(default=False)
    is_ph1_issued = models.BooleanField(default=False)
    is_ph2_issued = models.BooleanField(default=False)
    is_oio_issued = models.BooleanField(default=False)
    is_paused = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)


