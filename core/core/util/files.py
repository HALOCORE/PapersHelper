import os
from . import pdf
from . import tool
from . import datart

def files_get():
    pass

def files_cachefulltxt_get():
    pass

def file_summary_get(params):
    fname = params["filename"]
    summary = datart.file_summary_read(fname)
    if summary is None:
        summary = file_summary_gen(params)["summary"]
        datart.file_summary_write(fname, summary)
        summary = datart.file_summary_read(fname)
    return {"summary": summary}

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

###########################################

def file_summary_gen(params):
    summary = {
            "title": None,
            "source": None,
            "year": None,
            "authors": [],
            "institude": [],
            "keywords": []
            }
    fname = params["filename"]
    srcyear = fname.split('/')[-1].split('-')[0]
    summary["year"] = srcyear[-4:]
    summary["source"] = srcyear[:-4]
    pdf_result = pdf.pdf_text_get(params)
    txt = pdf_result['content'].strip()
    lines = txt.splitlines()
    summary["title"] = lines[0]
    absidx = tool.first_line_index(
        lines, lambda x : x.lower().find("abstract") >= 0)
    if absidx != -1:
        before_abs = tool.lines_trim(lines[:absidx])
        summary["institude"] = before_abs
    keysidx = tool.first_line_index(
        lines, lambda x : x.lower().find("keywords") >= 0)
    if absidx != -1:
        kws = (lines[keysidx] + lines[keysidx+1]).replace("Keywords", "").split(";")
        summary["keywords"] = tool.strip_elems(kws)
    return {"summary": summary}