from common.api_response import ApiResponse
from common.base_controller import BaseController
from common.model_serializer import ModelSerializer
from common.permission_checker import PermissionChecker
from nguoi_thue.services import TenantService

class TenantController(BaseController):
    def __init__(self):
        super().__init__(TenantService())

    def my_profile(self,request):
        print("HaiPham")
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)
        
        account , error = PermissionChecker.require_login(request)
        if error:
            return error
        
        try:
            tenant = self.service.get_my_profile(account)
            result = ModelSerializer.serialize_object(tenant)
            return ApiResponse.success_response(
                result,
                "Thông tin người thuê"
            )
        except Exception as ex:
            return ApiResponse.error_response(str(ex), 404)