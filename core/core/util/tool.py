import os
import json

def ensure_path(path):
    if not os.path.exists(path):
        print("# ensure_path CREATE: " + path)
        os.makedirs(path)

def rm_file_ext(fname:str):
    return "".join(fname.split('.')[:-1])

def ch_file_ext(fname:str, ext:str):
    return rm_file_ext(fname) + ext

def set_dict(mydict, keys, value):
    if len(keys) > 1:
        key = keys[0]
        rest_keys = keys[1:]
        if key not in mydict:
            mydict[key] = dict()
        set_dict(mydict[key], rest_keys, value)
    elif len(keys) == 1:
        mydict[keys[0]] = value
    else:
        raise ValueError("keys.length should > 1")

def get_dict_val(mydict, keys):
    if len(keys) > 1:
        key = keys[0]
        rest_keys = keys[1:]
        if key not in mydict:
            return None
        get_dict(mydict[key], rest_keys)
    elif len(keys) == 1:
        return mydict[keys[0]]
    else:
        return mydict

def first_line_index(lines:list, cond):
    for i in range(0, len(lines)):
        if cond(lines[i]):
            return i
    return -1

def lines_trim(lines:list):
    results = []
    i = 0
    for i in range(len(lines)):
        if lines[i].strip() != "":
            break
    if i == len(lines): return []
    for j in range(len(lines)-1, i, -1):
        if lines[j].strip() != "":
            break
    return lines[i:j+1]

def list_map(mylist:list, func):
    return [func(x) for x in mylist]

def strip_elems(mylist):
    return [x.strip() for x in mylist]

def TryReadJson(filename:str):
    result = None
    print("# TryReadJson: " + filename)
    if os.path.exists(filename):
        with open(filename) as f:
            result = json.load(f)
    return result

def WriteJson(filename:str, obj):
    print("# WriteJson: " + filename)
    ensure_path(os.path.dirname(filename))
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=2)

def TryReadTxt(filename:str):
    result = None
    print("# TryReadTxt: " + filename)
    if os.path.exists(filename):
        with open(filename) as f:
            result = f.read()
    return result

def WriteTxt(filename:str, myStr:str):
    print("# WriteTxt: " + filename)
    ensure_path(os.path.dirname(filename))
    with open(filename, 'w') as f:
        f.write(myStr)