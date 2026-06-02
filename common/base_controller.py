from common.api_response import ApiResponse
from common.model_serializer import ModelSerializer
from common.permission_checker import PermissionChecker
from common.request_reader import RequestReader 

class BaseController:
    def __init__(self, service):
        self.service = service
        print("self.serverice",self.service);

    def list(self, request):
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)

        account, error = PermissionChecker.require_landlord(request)

        print("account",account,"error",error)
        if error:
            return error

        data = ModelSerializer.serialize_queryset(self.service.get_all())
        print("data",data);
        return ApiResponse.success_response(data, "Lấy danh sách thành công")

    def detail(self, request, pk):
        if request.method != "GET":
            return ApiResponse.error_response("API này chỉ hỗ trợ GET", 405)

        account, error = PermissionChecker.require_landlord(request)

        if error:
            return error

        try:
            obj = self.service.get_detail(pk)
            data = ModelSerializer.serialize_object(obj)
            return ApiResponse.success_response(data, "Lấy chi tiết thành công")
        except Exception:
            return ApiResponse.error_response("Không tìm thấy dữ liệu", 404)

    def create(self, request):
        if request.method != "POST":
            return ApiResponse.error_response("API này chỉ hỗ trợ POST", 405)

        account, error = PermissionChecker.require_landlord(request)

        if error:
            return error

        data = RequestReader.read_json(request)

        if data is None:
            return ApiResponse.error_response("JSON không hợp lệ")

        try:
            obj = self.service.create(data)
            result = ModelSerializer.serialize_object(obj)
            return ApiResponse.success_response(result, "Thêm dữ liệu thành công", 201)
        except Exception as ex:
            return ApiResponse.error_response(f"Lỗi thêm dữ liệu: {str(ex)}")

    def update(self, request, pk):
        if request.method != "PUT":
            return ApiResponse.error_response("API này chỉ hỗ trợ PUT", 405)

        account, error = PermissionChecker.require_landlord(request)

        if error:
            return error

        data = RequestReader.read_json(request)

        if data is None:
            return ApiResponse.error_response("JSON không hợp lệ")

        try:
            obj = self.service.update(pk, data)
            result = ModelSerializer.serialize_object(obj)
            return ApiResponse.success_response(result, "Cập nhật dữ liệu thành công")
        except Exception as ex:
            return ApiResponse.error_response(f"Lỗi cập nhật dữ liệu: {str(ex)}")

    def delete(self, request, pk):
        if request.method != "DELETE":
            return ApiResponse.error_response("API này chỉ hỗ trợ DELETE", 405)

        account, error = PermissionChecker.require_landlord(request)

        if error:
            return error

        try:
            self.service.delete(pk)
            return ApiResponse.success_response(None, "Xóa dữ liệu thành công")
        except Exception:
            return ApiResponse.error_response("Không tìm thấy dữ liệu", 404)