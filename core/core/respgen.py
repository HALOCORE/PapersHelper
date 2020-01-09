from django.http import HttpResponse
import json

JSON_CONTENT_TYPE = 'application/json; charset=utf-8'

class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return json.JSONEncoder.default(self, obj)

def JsonResponse(data:dict):
    content = json.dumps(data, ensure_ascii=False, cls=MyJsonEncoder, indent=2)
    resp = HttpResponse(content, status=200, content_type=JSON_CONTENT_TYPE)
    resp['Access-Control-Allow-Origin'] = '*'
    resp['Access-Control-Allow-Methods'] = 'POST,GET'
    resp['Access-Control-Allow-Headers'] = 'Content-Type'
    return resp

def JsonResponseOK(msg=""):
    return JsonResponse({"status": "OK", "msg": msg})

def JsonResponseNotSupported(msg=""):
    return JsonResponse({"status": "NOT-SUPPORTED", "msg": msg})