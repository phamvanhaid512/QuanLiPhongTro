from common.api_response import ApiResponse
from common.base_controller import BaseController
from common.model_serializer import ModelSerializer
from common.permission_checker import PermissionChecker
from common.request_reader import RequestReader
from tai_khoan.services import AccountService, AuthService


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def register(self, request):
        if request.method != "POST":
            return ApiResponse.error_response("API này chỉ hỗ trợ POST", 405)

        data = RequestReader.read_json(request)

        if data is None:
            return ApiResponse.error_response("JSON không hợp lệ")

        try:
            account = self.auth_service.register(data)
            result = ModelSerializer.serialize_object(account)

            return ApiResponse.success_response(
                result,
                "Đăng ký tài khoản thành công",
                201
            )
        except Exception as ex:
            return ApiResponse.error_response(str(ex))

    def login(self, request):
        if request.method != "POST":
            return ApiResponse.error_response("API này chỉ hỗ trợ POST", 405)

        data = RequestReader.read_json(request)

        if data is None:
            return ApiResponse.error_response("JSON không hợp lệ")

        try:
            result = self.auth_service.login(data)
            return ApiResponse.success_response(result, "Đăng nhập thành công")
        except Exception as ex:
            return ApiResponse.error_response(str(ex), 401)

    def logout(self, request):
        if request.method != "POST":
            return  ApiResponse.error_response("API này chỉ hỗ trợ POST", 405)

        account, error = PermissionChecker.require_login(request)

        if error:
            return error

        self.auth_service.logout(account)
        return ApiResponse.success_response(None, "Đăng xuất thành công")


class AccountController(BaseController):
    def __init__(self):
        super().__init__(AccountService())