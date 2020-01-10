# runtime data here.
import os
from . import tool

_file_tree = {}
_folder_summary_dict = {}
_file_summary_dict = {}
_file_refs_dict = {}

FILENAME_GETTER = {
    "summary": lambda x : x
}

ROOT_PATH = "/mnt/c/Users/HP/Desktop/iotrules/papers"
TEST_PDF_FILENAME = "/2019/ICSE2019-autotap--AutoTap Synthesizing and Repairing Trigger-Action Programs Using LTL Properties.pdf"

def full_filename(pathpart:str, finalpart:str=None):
    global ROOT_PATH
    fname = os.path.join(ROOT_PATH, pathpart)
    if finalpart is not None:
        fname = os.path.join(fname, finalpart)
    return os.path.abspath(fname)

def file_summary_read(filename:str):
    pass

def file_summary_write(filename:str, summary):
    pass

def file_refs_read(filename:str):
    pass

def file_refs_write(filename:str, refs):
    pass

def file_fulltxt_read(filename:str):
    pass

def file_fulltxt_write(filename:str, fulltxt):
    pass

def folder_summary_read(foldername:str):
    pass

def folder_summary_write(foldername:str, summary):
    pass

def file_tree_cache_read(foldername:str):
    global _file_tree
    if foldername.strip() == "":
        return _file_tree
    parts = os.path.split(foldername)
    return tool.get_dict_val(_file_tree, parts)

def file_tree_cache_update(foldername:str, callroot=True):
    global _file_tree
    fname = full_filename(foldername)
    fds = os.listdir(fname)
    files = [
        os.path.join(foldername, f)
        for f in fds
        if os.path.isfile(full_filename(foldername, f))]
    
    dirs = {
        os.path.join(foldername, f) : file_tree_cache_update(os.path.join(foldername, f), False) 
        for f in fds
        if os.path.isdir(full_filename(foldername, f))}
    
    result = {"files": files, "dirs": dirs}
    if callroot:
        parts = os.path.split(foldername)
        if len(parts) >= 1:
            tool.set_dict(_file_tree, parts, result)
        else:
            _file_tree = result
        return "OK"
    return result