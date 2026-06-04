from django.db import models


class Invoice(models.Model):
    STATUS_CHOICES = [
        ("UNPAID", "Chưa thanh toán"),
        ("PAID", "Đã thanh toán"),
    ]

    invoice_code = models.CharField(max_length=20, primary_key=True)
    contract = models.ForeignKey(
        "hop_dong.Contract",
        on_delete=models.CASCADE,
        db_column="contract_code"
    )
    month = models.CharField(max_length=7)
    room_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    service_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="UNPAID")
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "hoa_don"

    def save(self, *args, **kwargs):
        self.total_amount = self.room_amount + self.service_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_code