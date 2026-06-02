from django.http import JsonResponse
class ApiResponse:
      @staticmethod 
      def success_response(data = None, message="Success",status = 200):
        return JsonResponse(
        {
            "success": True,
            "message": message,
            "data": data,
        },
        status=status,
        json_dumps_params={"ensure_ascii": False},
        )

      @staticmethod
      def error_response(message="Error", status=400):
        return JsonResponse(
            {
                "success": False,
                "message": message,
                "data": None,
            },
            status=status,
            json_dumps_params={"ensure_ascii": False},
        )