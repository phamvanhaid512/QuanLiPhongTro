from common.base_controller import BaseController
from nguoi_thue.services import TenantService

class TenantController(BaseController):
    def __init__(self):
        super().__init__(TenantService())