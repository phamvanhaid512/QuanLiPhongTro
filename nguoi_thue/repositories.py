from common.base_repository import BaseRepository
from nguoi_thue.models import Tenant


class TenantRepository(BaseRepository):
    def __init__(self):
        super().__init__(Tenant)

    def find_by_account(self,account):
        return self.model.objects.filter(account=account).first()