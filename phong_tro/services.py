from common.base_service import BaseService
from hop_dong.models import Contract
from nguoi_thue.models import Tenant
from phong_tro.repositories import RoomRepository
class RoomService(BaseService):
    def __init__(self):
        super().__init__(
            repository=RoomRepository(),
            pk_field="room_code",
            prefix="R"
        )
    
    def get_empty_rooms(self):
        return self.repository.find_empty_rooms()
    
    def get_my_rooms(self, account):
        tenant = Tenant.objects.filter(account=account).first()

        if not tenant:
            raise ValueError("Tài khoản chưa liên kết với người thuê")

        contracts = Contract.objects.filter(
            tenant=tenant,
            status="ACTIVE"
        )

        room_codes = contracts.values_list("room_id", flat=True)
        return self.repository.find_by_codes(room_codes)