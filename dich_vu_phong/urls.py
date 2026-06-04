from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from dich_vu_phong.controllers import (
    RentalServiceController,
    ServiceReadingController,
)


rental_service_controller = RentalServiceController()
service_reading_controller = ServiceReadingController()

urlpatterns = [
    path("rental-services/", csrf_exempt(rental_service_controller.list)),
    path("rental-services/create/", csrf_exempt(rental_service_controller.create)),
    path("rental-services/<str:pk>/", csrf_exempt(rental_service_controller.detail)),
    path("rental-services/update/<str:pk>/", csrf_exempt(rental_service_controller.update)),
    path("rental-services/delete/<str:pk>/", csrf_exempt(rental_service_controller.delete)),

    path("service-readings/my-readings/", csrf_exempt(service_reading_controller.my_readings)),
    path("service-readings/", csrf_exempt(service_reading_controller.list)),
    path("service-readings/create/", csrf_exempt(service_reading_controller.create)),
    path("service-readings/<str:pk>/", csrf_exempt(service_reading_controller.detail)),
    path("service-readings/update/<str:pk>/", csrf_exempt(service_reading_controller.update)),
    path("service-readings/delete/<str:pk>/", csrf_exempt(service_reading_controller.delete)),
]