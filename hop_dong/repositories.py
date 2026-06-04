from common.base_repository import BaseRepository
from hop_dong.models import Contract


class ContractRepository(BaseRepository):
    def __init__(self):
        super().__init__(Contract)


    def find_by_tenant(self, tenant):
        return self.model.objects.filter(tenant=tenant)

    def find_active_by_tenant(self, tenant):
        return self.model.objects.filter(
            tenant=tenant,
            status="ACTIVE"
        )