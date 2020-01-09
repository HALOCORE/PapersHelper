from django.http import HttpRequest, HttpResponse
from .respgen import JsonResponse, JsonResponseNotSupported, JsonResponseOK
from . import conf
import os

def api_conf(request:HttpRequest):
    if request.method == 'GET':
        d = dir(conf)
        return JsonResponse(d)
    else:
        return JsonResponseNotSupported()
    

def api_files(request:HttpRequest):
    if request.method == 'GET':
        fds = os.listdir(conf.ROOT_PATH)
        fullfds = [os.path.join(conf.ROOT_PATH, f) for f in fds]
        files = [f for f in fullfds if os.path.isfile(f)]
        dirs = [f for f in fullfds if os.path.isdir(f)]
        return JsonResponse({"files": files, "dirs": dirs})
    else:
        return JsonResponseNotSupported()

def api_pdfinfo(request:HttpRequest):
    if request.method == 'GET':
        fname = request.GET['filename']
        if fname == None:
            fname = conf.TEST_PDF_FILENAME
        