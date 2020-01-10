from django.http import HttpRequest, HttpResponse
from .respgen import handler_gen
from . import config
from . import util
from . import test
import os


api_test = handler_gen(test.test)

api_files = handler_gen(util.files.files_get)
api_files_cachefulltxt = None
api_file_summary = None
api_file_refs = None
api_file_check = None
api_file_fulltxt = None

api_folders = None
api_folder_summary = None
api_folder_summary_update = None
api_folder_summary_check = None

api_conf = None
