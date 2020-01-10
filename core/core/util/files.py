import os

def files_get():
    fds = os.listdir(config.ROOT_PATH)
    fullfds = [os.path.join(config.ROOT_PATH, f) for f in fds]
    files = [f for f in fullfds if os.path.isfile(f)]
    dirs = [f for f in fullfds if os.path.isdir(f)]
    return {"files": files, "dirs": dirs}

def files_cachefulltxt_get():
    pass

def file_summary_get(params):
    fname = params['filename']

def file_summary_check_get(params):
    fname = params['filename']

def file_refs_get(params):
    fname = params['filename']

def file_refs_link_get(params):
    fname = params['filename']

def file_refs_link_update(params):
    fname = params['filename']

def file_check_get(params):
    fname = params['filename']

def file_fulltxt_get(params):
    fname = params['filename']

