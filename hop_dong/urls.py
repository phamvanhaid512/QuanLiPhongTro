from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from hop_dong.controllers import ContractController


contract_controller = ContractController()

urlpatterns = [
    path("contracts/my-contracts/", csrf_exempt(contract_controller.my_contracts)),

    path("contracts/", csrf_exempt(contract_controller.list)),
    path("contracts/create/", csrf_exempt(contract_controller.create)),
    path("contracts/<str:pk>/", csrf_exempt(contract_controller.detail)),
    path("contracts/update/<str:pk>/", csrf_exempt(contract_controller.update)),
    path("contracts/delete/<str:pk>/", csrf_exempt(contract_controller.delete)),
]