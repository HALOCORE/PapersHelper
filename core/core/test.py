from . import util
from .util import datart

def pdf_test():
    return pdf_gettext("/mnt/c/_MySoftwares/test.pdf")

def datart_test():
    import json
    print(datart.file_tree_cache_update(""))
    print(json.dumps(datart.file_tree_cache_read(""), indent=2))

def test():
    return datart_test()
    # return pdf_test()

if __name__ == "__main__":
    test()


