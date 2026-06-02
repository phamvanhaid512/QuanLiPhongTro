from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from tai_khoan.controllers import AuthController, AccountController


auth_controller = AuthController()
account_controller = AccountController()

urlpatterns = [
    path("auth/register/", csrf_exempt(auth_controller.register)),
    path("auth/login/", csrf_exempt(auth_controller.login)),
    path("auth/logout/", csrf_exempt(auth_controller.logout)),

    path("accounts/", csrf_exempt(account_controller.list)),
    path("accounts/create/", csrf_exempt(account_controller.create)),
    path("accounts/<str:pk>/", csrf_exempt(account_controller.detail)),
    path("accounts/update/<str:pk>/", csrf_exempt(account_controller.update)),
    path("accounts/delete/<str:pk>/", csrf_exempt(account_controller.delete)),
]