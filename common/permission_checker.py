from tai_khoan.models import Account 
from common.api_response import ApiResponse

class PermissionChecker:
    @staticmethod
    # //chưa hiểu 
    def get_current_account(request):    
        auth_header = request.headers.get("Authorization", "")
        print("Authorization",auth_header)
        token = ""
        print("token",token)
        if auth_header.startswith("Token "):
            token = auth_header.replace("Token ", "", 1).strip()
            print("token1",token)
        else:
            token = request.headers.get("X-Auth-Token", "").strip()
            print("token2",token)
        if not token:
            return None 

        return Account.objects.filter(
            token=token,
            status="ACTIVE"
        ).first()
    
    @staticmethod
    def require_login(request):
        account = PermissionChecker.get_current_account(request)
        print("account_service",account)
        if not account:
            return None, ApiResponse.error_response(
                "Ban chưa đăng nhập hoặc token không hợp lệ ",
                401
            )
        return account,None
    
    @staticmethod
    def require_landlord(request):
        account, error = PermissionChecker.require_login(request)

        if error:
            return None, error
        
        if account.role != "LANDLORD":
            return None, ApiResponse.error_response(
                "Bạn không có quyền thực hiện hành động này",
                403
            )
        
        return account, None
    
