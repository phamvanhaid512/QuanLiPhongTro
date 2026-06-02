
# Create your models here.
from django.db import models


class Tenant(models.Model):
    tenant_code = models.CharField(max_length=20, primary_key=True)
    account = models.OneToOneField(
        "tai_khoan.Account",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="account_code"
    )
    full_name = models.CharField(max_length=100)
    citizen_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "nguoi_thue"

    def __str__(self):
        return self.full_name