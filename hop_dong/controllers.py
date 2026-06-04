from common.base_controller import BaseController
from hop_dong.services import ContractService
from common.api_response import ApiResponse
from common.model_serializer import ModelSerializer
from common.permission_checker import PermissionChecker


class ContractController(BaseController):
    def __init__(self):
        super().__init__(ContractService())

    def my_contracts(self, request):
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)
        
        print("Toiw dau")
        account, error = PermissionChecker.require_login(request)

        if error:
            return error
        
        try: 
            contracts = self.service.get_my_contracts(account)
            result = ModelSerializer.serialize_queryset(contracts)
            return ApiResponse.success_response(
                result,
                "Danh sách hợp đồng của tôi",
            )
        except Exception as ex:
            return ApiResponse.error_response(str(ex), 404)