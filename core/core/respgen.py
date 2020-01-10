from django.http import HttpRequest, HttpResponse
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

def JsonResponseSimple(status="OK", msg=""):
    return JsonResponse({"status": status, "msg": msg})

def handler_gen(getfunc, postfunc=None):
    ret_handler = def handler(request:HttpRequest):
        result = {}
        if request.method == 'GET':
            params = request.GET.dict()
            result == getfunc(params)
        elif postfunc is not None and request.method == 'POST':
            params = request.POST.dict()
            result == postfunc(params)
        if result is str:
            return JsonResponseSimple(result)
        else:
            result["status"] = "OK"
            return JsonResponse(result)
    return ret_handler