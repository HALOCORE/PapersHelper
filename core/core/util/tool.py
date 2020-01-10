def ensure_path(path):
    if not os.path.exists(path):
        print("# ensure_path CREATE: " + path)
        os.makedirs(path)

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