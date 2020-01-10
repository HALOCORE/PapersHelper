from django.http import HttpRequest, HttpResponse
from .respgen import handler_gen
from . import util
from . import test
import os


api_test = handler_gen(test.test)

api_reload = handler_gen(util.reloads.reloads_get)

api_filetree = handler_gen(util.files.filetree_get)
api_filetree_update = handler_gen(util.files.filetree_update)

api_file_summary = handler_gen(util.files.file_summary_get)
api_file_refs = handler_gen(util.files.file_refs_get)
api_file_fulltxt = handler_gen(util.files.file_fulltxt_get)
api_file_check = None

api_folders = None
api_folder_summary = None
api_folder_summary_update = None
api_folder_summary_check = None

api_conf = None
