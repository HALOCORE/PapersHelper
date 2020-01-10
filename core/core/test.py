import json
from .util import datart
from .util import pdf
from .util import files

def pdf_test():
    print(
        pdf.pdf_text_get({
            "filename": "2016/BuildSys2016-Systematically Debugging IoT Control System Correctness.pdf"
            })['content'])

def summary_test():
    result = files.file_summary_get(
        {
            "filename": "2016/BuildSys2016-Systematically Debugging IoT Control System Correctness.pdf"
        })
    print(json.dumps(result, indent=2))

def file_tree_test():
    print(datart.file_tree_cache_update(""))
    print(json.dumps(datart.file_tree_cache_read(""), indent=2))

def test():
    # return file_tree_test()
    # return pdf_test()
    summary_test()

if __name__ == "__main__":
    test()


