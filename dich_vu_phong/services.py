from common.base_service import BaseService
from dich_vu_phong.repositories import (
    RentalServiceRepository,
    ServiceReadingRepository,
)
from hop_dong.models import Contract
from nguoi_thue.models import Tenant


class RentalServiceService(BaseService):
    def __init__(self):
        super().__init__(
            repository=RentalServiceRepository(),
            pk_field="service_code",
            prefix="S"
        )


class ServiceReadingService(BaseService):
    def __init__(self):
        super().__init__(
            repository=ServiceReadingRepository(),
            pk_field="reading_code",
            prefix="RD"
        )

    def get_my_readings(self, account):
        tenant = Tenant.objects.filter(account=account).first()

        if not tenant:
            raise ValueError("Tài khoản chưa liên kết với người thuê")

        contracts = Contract.objects.filter(tenant=tenant)
        room_codes = contracts.values_list("room_id", flat=True)

        return self.repository.find_by_room_codes(room_codes)