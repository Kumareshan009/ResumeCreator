from SimpleTemplate import SimpleTemplate

st=SimpleTemplate()
st.addpage()
st.pages[0].settext(st.pages[0], "SSSSSSS")
print(st.pdf.page_no())
st.addpage()
st.save("D:\simple_demo.pdf")