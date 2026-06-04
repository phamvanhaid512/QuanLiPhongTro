from decimal import Decimal
from django.db import models


class RentalService(models.Model):
    service_code = models.CharField(max_length=20, primary_key=True)
    service_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    unit_name = models.CharField(max_length=50)
    note = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "dich_vu"

    def __str__(self):
        return self.service_name


class ServiceReading(models.Model):
    reading_code = models.CharField(max_length=20, primary_key=True)
    room = models.ForeignKey(
        "phong_tro.Room",
        on_delete=models.CASCADE,
        db_column="room_code"
    )
    rental_service = models.ForeignKey(
        "dich_vu_phong.RentalService",
        on_delete=models.CASCADE,
        db_column="service_code"
    )
    month = models.CharField(max_length=7)
    old_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    new_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = "chi_so_dich_vu"

    def save(self, *args, **kwargs):
            self.quantity = self.new_value - self.old_value

            if self.quantity < 0:
                self.quantity = Decimal("0")

            self.amount = self.quantity * self.rental_service.unit_price
            super().save(*args, **kwargs)

    def __str__(self):
            return f"{self.room_id} - {self.rental_service_id} - {self.month}"