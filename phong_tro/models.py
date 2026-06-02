from django.db import models

class Room(models.Model):
    STATUS_CHOICES = [
        ("EMPTY","Trống"),
        ("RENTED", "Đang thuê"),
        ("MAINTENANCE", "Bảo trì"),
    ]

    room_code = models.CharField(max_length=20,primary_key=True)
    room_name = models.CharField(max_length=100)
    area = models.FloatField(default=0)
    rent_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="EMPTY")

    class Meta:
        db_table = "phong_tro"

    def __str__(self):
        return self.room_name
# Create your models here.
