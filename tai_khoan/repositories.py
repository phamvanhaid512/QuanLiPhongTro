from common.base_repository import BaseRepository
from tai_khoan.models import Account

class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__(Account)

    def find_by_username(self,username):
        return self.model.objects.filter(username=username).first()
    
    def find_by_token(self,token):
        return self.model.objects.filter(
            token=token,
            status = "ACTIVE"
        ).first()