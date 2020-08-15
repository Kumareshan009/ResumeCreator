from Page import Page

class A4Page(Page):
	def __init__(this, pdf):
		super(A4Page, this).__init__(210, 297, pdf)
        
