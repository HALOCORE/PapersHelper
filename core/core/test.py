from . import util
from .util import datart
from .util import pdf

def pdf_test():
    print(
        pdf.pdf_text_get({
            "filename": "2016/CHI2019REF34-BuildSys16-Systematically Debugging IoT Control System Correctness.pdf"
            }))

def datart_test():
    import json
    #print(datart.file_tree_cache_update(""))
    #print(json.dumps(datart.file_tree_cache_read(""), indent=2))

def test():
    # return datart_test()
    return pdf_test()

if __name__ == "__main__":
    test()


