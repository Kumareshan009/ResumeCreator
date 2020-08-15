class LayoutDefinition:
    def __init__(this, xstart, ystart, width, height, padding):
        this.x=xstart+padding.left
        this.y=ystart+padding.top
        this.width=width-padding.right-padding.left
        this.height=height-padding.bottom-padding.top