class Padding:
	def __init__(this, left, top, right, bottom):
		this.left=left;
		this.top=top;
		this.bottom=bottom;
		this.right=right
		
class DefaultPadding(Padding):
	def __init__(this):
		super(DefaultPadding, this).__init__(0,0,0,0)
		
class EqualPadding(Padding):
	def __init__(this, pad):
		super(EqualPadding, this).__init__(pad, pad, pad, pad)
        
class HVPadding(Padding):
    def __init__(this, hPad, vPad):
        super(HVPadding, this).__init__(hpad, vPad, hPad, vPad)