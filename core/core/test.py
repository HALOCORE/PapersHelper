import json
from .util import datart
from .util import pdf
from .util import files
from .util import reloads

FNAME1 = "2016/BuildSys2016-Systematically Debugging IoT Control System Correctness.pdf"

def pdf_test():
    print(
        pdf.pdf_text_get({
            "fileid": FNAME1
            })['content'])

def summary_test():
    result = files.file_summary_get(
        {
            "fileid": FNAME1
        })
    print(json.dumps(result, indent=2))

def ref_test():
    result = files.file_refs_get({
        "fileid": FNAME1
    })
    print(json.dumps(result, indent=2))


def file_tree_test():
    print(datart.file_tree_cache_update(""))
    print(json.dumps(datart.file_tree_cache_read(""), indent=2))

def reload_test():
    reloads.reloads_get()


def test():
    # return file_tree_test()
    # return pdf_test()
    summary_test()
    # ref_test()
    # reload_test()

if __name__ == "__main__":
    test()


