from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# from hoa_don.controllers import InvoiceController


# invoice_controller = InvoiceController()

urlpatterns = [
    # path("invoices/calculate/", csrf_exempt(invoice_controller.calculate_invoice)),
    # path("invoices/pay/<str:invoice_code>/", csrf_exempt(invoice_controller.mark_as_paid)),
    # path("invoices/my-invoices/", csrf_exempt(invoice_controller.my_invoices)),
    # path("invoices/my-invoices/<str:invoice_code>/", csrf_exempt(invoice_controller.my_invoice_detail)),

    # path("invoices/", csrf_exempt(invoice_controller.list)),
    # path("invoices/create/", csrf_exempt(invoice_controller.create)),
    # path("invoices/<str:pk>/", csrf_exempt(invoice_controller.detail)),
    # path("invoices/update/<str:pk>/", csrf_exempt(invoice_controller.update)),
    # path("invoices/delete/<str:pk>/", csrf_exempt(invoice_controller.delete)),
]