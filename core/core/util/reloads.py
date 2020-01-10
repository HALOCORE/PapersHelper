from . import files
from . import folders
from . import datart


def _reloads_file(fileid):
    files.file_fulltxt_get({"fileid": fileid})
    files.file_summary_get({"fileid": fileid})
    files.file_refs_get({"fileid": fileid})

def _reloads_rec(dirdict):
    for fileid in dirdict["files"]:
        _reloads_file(fileid)
    for dirname in dirdict["dirs"].keys():
        _reloads_rec(dirdict["dirs"][dirname])

def reloads_get(params=None):
    datart.clear()
    filetree = files.filetree_update()
    _reloads_rec(filetree["filetree"])
    return "OK"
