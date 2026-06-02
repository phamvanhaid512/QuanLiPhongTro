from common.base_repository import BaseRepository
from phong_tro.models import Room
class RoomRepository(BaseRepository):
    def __init__(self):
        super().__init__(Room)

    def find_empty_rooms(self):
        return self.model.objects.filter(status = "EMPTY")