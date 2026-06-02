from django.db import models


class Account(models.Model):
    ROLE_CHOICES = [
        ("LANDLORD", "Chủ trọ"),
        ("TENANT", "Người thuê"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Hoạt động"),
        ("LOCKED", "Khóa"),
    ]

    account_code = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
    token = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "tai_khoan"

    def __str__(self):
        return f"{self.username} - {self.role}"