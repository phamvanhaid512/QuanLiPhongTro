from common.api_response import ApiResponse
from common.base_controller import BaseController
from common.model_serializer import ModelSerializer
from common.permission_checker import PermissionChecker
from dich_vu_phong.services import (
    RentalServiceService,
    ServiceReadingService,
)


class RentalServiceController(BaseController):
    def __init__(self):
        super().__init__(RentalServiceService())


class ServiceReadingController(BaseController):
    def __init__(self):
        super().__init__(ServiceReadingService())

    def my_readings(self, request):
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)

        account, error = PermissionChecker.require_login(request)

        if error:
            return error

        try:
            readings = self.service.get_my_readings(account)

            result = ModelSerializer.serialize_queryset(readings)

            return ApiResponse.success_response(
                result,
                "Danh sách chỉ số dịch vụ của tôi"
            )
        except Exception as ex:
            return ApiResponse.error_response(str(ex), 404)