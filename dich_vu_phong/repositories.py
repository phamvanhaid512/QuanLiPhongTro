from common.base_repository import BaseRepository
from dich_vu_phong.models import RentalService, ServiceReading


class RentalServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__(RentalService)


class ServiceReadingRepository(BaseRepository):
    def __init__(self):
        super().__init__(ServiceReading)

    def find_by_room_codes(self, room_codes):
        return self.model.objects.filter(room_id__in=room_codes)

    def find_by_room_and_month(self, room, month):
        return self.model.objects.filter(
            room=room,
            month=month
        )