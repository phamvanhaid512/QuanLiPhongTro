from common.base_service import BaseService
from hop_dong.repositories import ContractRepository
from nguoi_thue.models import Tenant


class ContractService(BaseService):
    def __init__(self):
        super().__init__(
            repository=ContractRepository(),
            pk_field="contact_code",
            prefix="CT"
            )
        
    def create(self, data):
        contract = super().create(data)

        room = contract.room
        room.status = "RENTED"
        room.save()

        return contract

    def get_my_contracts(self, account):
        tenant = Tenant.objects.filter(account=account).first()
        print("tenat_123",tenant)
        if not tenant:
            raise ValueError("Tài khoản chưa liên kết với người thuê")

        return self.repository.find_by_tenant(tenant)