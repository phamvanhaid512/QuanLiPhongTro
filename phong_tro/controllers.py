from common.api_response import ApiResponse
from common.base_controller import BaseController
from common.model_serializer import ModelSerializer
from common.permission_checker import PermissionChecker
from phong_tro.services import RoomService
class RoomController(BaseController):
    def __init__(self):
        super().__init__(RoomService())

    def empty_rooms(self,request):
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)
        
        rooms = self.service.get_empty_rooms()
        result = ModelSerializer.serialize_queryset(rooms)

        return ApiResponse.success_response(
            result,
            "Danh sách phòng trống"
        )
    
    def get_empty_rooms(self):
        return self.repository.find_empty_rooms()

    def my_rooms(self, request):
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)

        account, error = PermissionChecker.require_login(request)

        if error:
            return error

        try:
            rooms = self.service.get_my_rooms(account)
            result = ModelSerializer.serialize_queryset(rooms)

            return ApiResponse.success_response(
                result,
                "Danh sách phòng của tôi"
            )
        except Exception as ex:
            return ApiResponse.error_response(str(ex), 404)