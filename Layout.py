from LayoutDefinition import LayoutDefinition
from Padding import DefaultPadding 
from Padding import EqualPadding 

class Layout:
    def __init__(this, xstart, ystart, width, height, pdf):
        this.actualDef=LayoutDefinition(xstart, ystart, width, height, DefaultPadding())
        this.pdf=pdf
        this.updatepadding(EqualPadding(0.5))
        
    def setpadding(this, padding):
        this.updatepadding(padding)
        
    def setbackground(this, color):
        this.pdf.set_fill_color(color[0], color[1], color[2])
        this.pdf.rect(this.paddedDef.x, this.paddedDef.y, this.paddedDef.width, this.paddedDef.height, 'F')
        
    def updatepadding(this, padding):
        this.paddedDef=LayoutDefinition(this.actualDef.x, this.actualDef.y, this.actualDef.width, this.actualDef.height, padding)
        this.currentX=this.paddedDef.x
        this.currentY=this.paddedDef.y
        
    def relocateY(this, deltay):
        this.actualDef.y=this.actualDef.y-deltay
        this.paddedDef.y=this.paddedDef.y-deltay
        this.currentY=this.currentY-deltay

        
	