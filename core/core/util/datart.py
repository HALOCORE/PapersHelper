# runtime data here.
import os
from . import tool

_file_tree = {}
_folder_summary_dict = {}
_file_summary_dict = {}
_file_refs_dict = {}
_file_fulltxt_dict = {}

ROOT_PATH = "/mnt/c/Users/HP/Desktop/iotrules/papers"

def full_filename(pathpart:str, finalpart:str=None):
    fullname = os.path.join(ROOT_PATH, pathpart)
    if finalpart is not None:
        fullname = os.path.join(fullname, finalpart)
    return os.path.abspath(fullname)

FILENAME_GETTER = {
    "file_summary": lambda x : full_filename(tool.ch_file_ext(x, ".summary.md")),
    "file_refs": lambda x : full_filename(tool.ch_file_ext(os.path.join(
        os.path.join(os.path.dirname(x), "_refs"),
        os.path.basename(x)), ".refs.json")),
    "file_fulltxt": lambda x : full_filename(tool.ch_file_ext(os.path.join(
        os.path.join(os.path.dirname(x), "_txt"),
        os.path.basename(x)), ".txt")),
    "folder_summary": lambda x : full_filename(os.path.join(x, "summary.md")),
}

def clear():
    global _file_fulltxt_dict
    global _file_refs_dict
    global _file_summary_dict
    global _file_tree
    global _folder_summary_dict
    _file_tree = {}
    _folder_summary_dict = {}
    _file_summary_dict = {}
    _file_refs_dict = {}
    _file_fulltxt_dict = {}

def file_summary_read(fileid:str):
    global _file_summary_dict
    if fileid in _file_summary_dict:
        return _file_summary_dict[fileid]
    fullname = FILENAME_GETTER["file_summary"](fileid)
    _file_summary_dict[fileid] = tool.TryReadJson(fullname)
    return _file_summary_dict[fileid]

def file_summary_write(fileid:str, summary):
    global _file_summary_dict
    fullname = FILENAME_GETTER["file_summary"](fileid)
    tool.WriteJson(fullname, summary)
    _file_summary_dict[fileid] = tool.TryReadJson(fullname)
    return _file_summary_dict[fileid]

def file_refs_read(fileid:str):
    global _file_refs_dict
    if fileid in _file_refs_dict:
        return _file_refs_dict[fileid]
    fullname = FILENAME_GETTER["file_refs"](fileid)
    _file_refs_dict[fileid] = tool.TryReadJson(fullname)
    return _file_refs_dict[fileid]

def file_refs_write(fileid:str, refs):
    global _file_refs_dict
    fullname = FILENAME_GETTER["file_refs"](fileid)
    tool.WriteJson(fullname, refs)
    _file_refs_dict[fileid] = tool.TryReadJson(fullname)
    return _file_refs_dict[fileid]

def file_fulltxt_read(fileid:str):
    global _file_fulltxt_dict
    if fileid in _file_fulltxt_dict:
        return _file_fulltxt_dict[fileid]
    fullname = FILENAME_GETTER["file_fulltxt"](fileid)
    _file_fulltxt_dict[fileid] = tool.TryReadTxt(fullname)
    return _file_fulltxt_dict[fileid]

def file_fulltxt_write(fileid:str, fulltxt):
    global _file_fulltxt_dict
    fullname = FILENAME_GETTER["file_fulltxt"](fileid)
    tool.WriteTxt(fullname, fulltxt)
    _file_fulltxt_dict[fileid] = tool.TryReadTxt(fullname)
    return _file_fulltxt_dict[fileid]

def folder_summary_read(folderid:str):
    pass

def folder_summary_write(folderid:str, summary):
    pass

def file_tree_cache_read(folderid:str):
    global _file_tree
    if folderid is None or folderid.strip() == "":
        return _file_tree
    parts = os.path.split(folderid)
    return tool.get_dict_val(_file_tree, parts)

def file_tree_cache_update(folderid:str, callroot=True):
    global _file_tree
    fullname = full_filename(folderid)
    fds = os.listdir(fullname)
    files = [
        os.path.join(folderid, f)
        for f in fds
        if f.endswith(".pdf") and os.path.isfile(full_filename(folderid, f))]
    
    dirs = {
        os.path.join(folderid, f) : file_tree_cache_update(os.path.join(folderid, f), False) 
        for f in fds
        if not f.endswith("_refs") and not f.endswith("_txt") and os.path.isdir(full_filename(folderid, f))}
    
    result = {"files": files, "dirs": dirs}
    if callroot:
        if folderid.strip() == "":
            _file_tree = result
        else:
            parts = os.path.split(folderid)
            raise ValueError("Not Supported Yet.")
        return _file_tree
    return result