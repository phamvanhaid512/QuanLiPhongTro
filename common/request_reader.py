import json

class RequestReader:
    @staticmethod
    def read_json(request):
        try:
            if not request.body:
                return {}
            return json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return None