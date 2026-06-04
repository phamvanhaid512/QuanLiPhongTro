from common.base_service import BaseService
from nguoi_thue.repositories import TenantRepository


class TenantService(BaseService):
    def __init__(self):
        super().__init__(
            repository=TenantRepository(),
            pk_field="tenant_code",
            prefix="NT"
        )

    def get_my_profile(self,account):
        tenant = self.repository.find_by_account(account)
        print("accountService",account)

        print("TenantService",tenant)

        if not tenant:
            raise ValueError("Tài khoản chưa liên kết với người thuê")
        
        return tenant