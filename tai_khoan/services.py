import uuid
from django.contrib.auth.hashers import make_password, check_password
from common.base_service import BaseService
from tai_khoan.repositories import AccountRepository


class AuthService:
    def __init__(self):
        self.account_repository = AccountRepository()

    def generate_account_code(self):
        index = self.account_repository.model.objects.count() + 1

        while True:
            code = f"AC{index:03d}"

            if not self.account_repository.exists(account_code=code):
                return code

            index += 1

    def register(self, data):
        username = data.get("username")
        password = data.get("password")
        full_name = data.get("full_name")
        role = data.get("role", "TENANT")

        if not username or not password or not full_name:
            raise ValueError("Thiếu username, password hoặc full_name")

        if role not in ["LANDLORD", "TENANT"]:
            raise ValueError("role chỉ được là LANDLORD hoặc TENANT")

        if self.account_repository.find_by_username(username):
            raise ValueError("Username đã tồn tại")

        account = self.account_repository.create(
            account_code=data.get("account_code", self.generate_account_code()),
            username=username,
            password=make_password(password),
            full_name=full_name,
            role=role,
            status="ACTIVE",
        )

        return account
    
    def login(self,data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise ValueError("Thiếu username hoặc password")
        
        account = self.account_repository.find_by_username(username)

        if not account:
            raise ValueError("Tài khoản không tồn tại")

        if account.status != "ACTIVE":
            raise ValueError("Tài khoản đã bị khóa")

        if not check_password(password, account.password):
            raise ValueError("Mật khẩu không đúng")
        
        token = str(uuid.uuid4())
        account.token = token
        account.save()

        account.save()

        return {
            "account_code": account.account_code,
            "username": account.username,
            "full_name": account.full_name,
            "role": account.role,
            "token": token,
        }
    
    def logout(self, account):
        account.token = None
        account.save()
        return True
    
class AccountService(BaseService):
    def __init__(self):
        super().__init__(
            repository=AccountRepository(),
            pk_field="account_code",
            prefix="AC"
        )

    def prepare_data(self, data, auto_generate_pk=True):
        result = super().prepare_data(data, auto_generate_pk)

        if "password" in result:
            if not str(result["password"]).startswith("pbkdf2_"):
                result["password"] = make_password(result["password"])

        return result
    