from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
import sys

rsrcmgr = PDFResourceManager()

def pdf_gettext(filename):
    outfp = sys.stdout
    device = TextConverter(rsrcmgr, outfp, laparams=LAParams())
    with open(filename, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    device.close()