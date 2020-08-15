from A4 import A4

class SimpleTemplate(A4):

    def __init__(this):
        super(SimpleTemplate, this).__init__()
        this.partition()
        this.partitionFirstColoumn()
    
    def partition(this):
        this.pages[0].createsections([1],[1,2])
        this.pages[0].sections[0][0].setbackground([90,89, 9])
        this.pages[0].sections[0][1].setbackground([255,89, 9])
        
    def partitionFirstColoumn(this):
        firstcol=this.pages[0].sections[0][0]
        firstcol.createsections([1,1,1],[1])
        firstcol.sections[0][0].setbackground([90,89, 9])
        firstcol.sections[1][0].setbackground([255,89, 9])
        firstcol.sections[2][0].setbackground([255,89, 255])

