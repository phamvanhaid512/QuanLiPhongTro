from django.db import models


class Contract(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Còn hiệu lực"),
        ("ENDED", "Đã kết thúc"),
    ]

    contract_code = models.CharField(max_length=20, primary_key=True)
    room = models.ForeignKey(
        "phong_tro.Room",
        on_delete=models.CASCADE,
        db_column="room_code"
    )
    tenant = models.ForeignKey(
        "nguoi_thue.Tenant",
        on_delete=models.CASCADE,
        db_column="tenant_code"
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    deposit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")

    class Meta:
        db_table = "hop_dong"

    def __str__(self):
        return self.contract_code