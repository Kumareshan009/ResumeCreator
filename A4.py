from SimplePDF import SimplePDF
from A4Page import A4Page

class A4(SimplePDF):
    def __init__(this):
        super(A4, this).__init__('P', 'mm', 'A4')
        this.addpage()
        
    def addpage(this):
        this.pages.append(A4Page(this.pdf))
