from . import util

def pdf_test():
    return pdf_gettext("/mnt/c/_MySoftwares/test.pdf")


def test():
    return pdf_test()

if __name__ == "__main__":
    result = test()
    print(result)


