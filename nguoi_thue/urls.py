from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from nguoi_thue.controllers import TenantController


tenant_controller = TenantController()

urlpatterns = [
    path("tenants/my-profile/", csrf_exempt(tenant_controller.my_profile)),

    path("tenants/", csrf_exempt(tenant_controller.list)),
    path("tenants/create/", csrf_exempt(tenant_controller.create)),
    path("tenants/<str:pk>/", csrf_exempt(tenant_controller.detail)),
    path("tenants/update/<str:pk>/", csrf_exempt(tenant_controller.update)),
    path("tenants/delete/<str:pk>/", csrf_exempt(tenant_controller.delete)),
]