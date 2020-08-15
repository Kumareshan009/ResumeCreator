from Section import Section
from Padding import Padding
from Layout import Layout
from fpdf import FPDF

class Page(Section):
    def __init__(this, width, height, pdf):
        super(Page, this).__init__(0,0,width,height,pdf)
        this.pdf.add_page()
        this.pdf.set_auto_page_break(False, 0)

    def settext(this, section, text):
         fontsiz=14
         this.pdf.set_y(section.currentY)
         this.pdf.set_x(section.currentX)
         print(str(section.currentX)+" "+str(section.currentY))
         this.pdf.set_font("Arial", size=fontsiz)
         this.pdf.cell(this.pdf.get_string_width(text), fontsiz*0.4, txt=text, ln=2)
         this.currentY=this.pdf.get_y()
        