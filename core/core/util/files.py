import os
import re
from . import pdf
from . import tool
from . import datart

def filetree_get(params=None):
    filetree = datart.file_tree_cache_read("")
    return {"filetree": filetree}

def filetree_update(params=None):
    filetree = datart.file_tree_cache_update("")
    return {"filetree": filetree}

def file_search_get(params=None):
    files = datart.file_search()
    return {"files": files}

def file_summary_get(params):
    fileid = params['fileid']
    summary = datart.file_summary_read(fileid)
    if summary is None:
        summary = file_summary_gen(params)["summary"]
        summary = datart.file_summary_write(fileid, summary)
    return {"summary": summary}

def file_summary_check_get(params):
    fileid = params['fileid']
    return {}

def file_refs_get(params):
    fileid = params['fileid']
    refs = datart.file_refs_read(fileid)
    if refs is None:
        refs = file_refs_gen(params)["refs"]
        refs = datart.file_refs_write(fileid, refs)
    return {"refs": refs}


def file_refs_link_get(params):
    fileid = params['fileid']

def file_refs_link_update(params):
    fileid = params['fileid']

def file_check_get(params):
    fileid = params['fileid']

def file_fulltxt_get(params):
    fileid = params['fileid']
    fulltxt = datart.file_fulltxt_read(fileid)
    if fulltxt is None:
        fulltxt = pdf.pdf_text_get(params)['content']
        fulltxt = datart.file_fulltxt_write(fileid, fulltxt)
    return {"fulltxt": fulltxt}

###########################################

def file_summary_gen(params):
    summary = {
            "confirmed": False,
            "title": None,
            "source": None,
            "year": None,
            "authors": [],
            "institude": [],
            "keywords": []
            }
    
    fileid = params["fileid"]
    srcyear = fileid.split('/')[-1].split('-')[0]
    summary["year"] = srcyear[-4:]
    summary["source"] = srcyear[:-4]
    
    txt = file_fulltxt_get(params)["fulltxt"]
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


def file_refs_gen(params):
    refs = {
        "confirmed": False,
        "entries": []
    }
    txt = file_fulltxt_get(params)["fulltxt"]
    lines = txt.splitlines()
    absidx = tool.first_line_index(
        lines, lambda x : x.lower().endswith("references"))
    reflines = tool.lines_trim(lines[absidx + 1:])
    refstrs = []
    refnos = []
    current_ref = ""
    for refline in reflines:
        rl = refline.strip()
        if rl == "": continue
        pos = re.search(r"\[\d{1,3}\]", rl)
        if pos != None:
            if current_ref != "": refstrs.append(current_ref)
            refnos.append(int(pos.group(0)[1:-1]))
            current_ref = rl[len(pos.group(0)):]
        else:
            current_ref += rl + " "
    if current_ref != "": refstrs.append(current_ref)
    if len(refnos) != len(refstrs): print("# [WARN] references counting error.")
    refs["entries"] = [(no, s) for no, s in zip(refnos, refstrs)]
    return {"refs": refs}
