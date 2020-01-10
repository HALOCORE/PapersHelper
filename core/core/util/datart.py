# runtime data here.

_file_tree = {}
_folder_summary_dict = {}
_file_summary_dict = {}
_file_refs_dict = {}

FILENAME_GETTER = {
    "summary": lambda x : x
}

def file_summary_read(filename):
    pass

def file_summary_write(filename, summary):
    pass

def file_refs_read(filename):
    pass

def file_refs_write(filename, refs):
    pass

def file_fulltxt_read(filename):
    pass

def file_fulltxt_write(filename, fulltxt):
    pass

def folder_summary_read(foldername):
    pass

def folder_summary_write(foldername, summary):
    pass

def file_tree_cache_read(foldername):
    pass

def file_tree_cache_update(foldername):
    pass
