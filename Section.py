from Layout import Layout
from Padding import Padding

class Section(Layout):
    def __init__(this, xstart, ystart, width, height, pdf):
        super(Section, this).__init__(xstart, ystart, width, height, pdf)
        this.sections=[]

    def getTotal(this, definitions):
        t=0;
        for i in range(0, len(definitions)):
         t=t+definitions[i]
        return t
        
    def createsections(this, rowdefinitions, coldefinitions):
        this.sections=[]
        rth=this.getTotal(rowdefinitions)
        ctw=this.getTotal(coldefinitions)
        cy=this.paddedDef.y
        for i in range(0, len(rowdefinitions)):
            this.sections.append([])
            crh=(this.paddedDef.height*rowdefinitions[i])/rth
            cx=this.paddedDef.x
            for j in range(0, len(coldefinitions)):
                ccw=(this.paddedDef.width*coldefinitions[j])/ctw
                print(str(i)+" "+str(j)+" "+str(cx)+" "+str(cy)+" "+str(ccw)+" "+str(crh))
                section=Section(cx, cy, ccw, crh, this.pdf)
                section.setpadding(Padding(1, 0.5, 0.5, 0.5))
                this.sections[i].append(section)
                cx=cx+ccw
            cy=cy+crh


        
	