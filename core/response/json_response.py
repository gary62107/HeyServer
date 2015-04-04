from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class JSONResponse():
    def __init__(self):
        pass

    @classmethod
    def success(cls, json_result=None):
        json_object = {
            "status": "success"
        }

        if json_result is not None:
            json_object["result"] = json_result

        return cls.response(json_object, status.HTTP_200_OK)

    @classmethod
    def error(cls, error_message):
        json_object = {
            "status": "fail",
            "result": error_message
        }
        return cls.response(json_object, status.HTTP_403_FORBIDDEN)

    @staticmethod
    def response(json_object, response_status):
        return HttpResponse(JSONRenderer().render(json_object), status=response_status, content_type="application/json")
