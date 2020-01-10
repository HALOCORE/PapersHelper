from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
import sys
import io
from . import datart


rsrcmgr = PDFResourceManager()

def pdf_text_get(params):
    fileid = params["fileid"]
    fullname = datart.full_filename(fileid)
    outfp = io.StringIO()
    device = TextConverter(rsrcmgr, outfp, laparams=LAParams())
    with open(fullname, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    device.close()
    contents = outfp.getvalue().replace('\ufb01', 'fi')
    outfp.close()
    return {"content": contents}

def pdf_meta_get(params):
    fileid = params["fileid"]
    return {}