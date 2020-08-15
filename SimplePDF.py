from fpdf import FPDF

class SimplePDF:

    def __init__(this, o, u, f):
        this.pdf=FPDF(orientation=o, unit=u, format=f)
        this.pages=[]
        
    def save(this, fileName):
        this.pdf.output(fileName)