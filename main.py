from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P',unit='mm',format='a4')
pdf.set_auto_page_break(auto=False,margin=0)
df = pd.read_csv('topics.csv')
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(10,1,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)
    for i in range(25,280,10):
        pdf.line(13,i,195,i)

    #set the footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='R')


    for i in range(row['Pages']-1):
        pdf.add_page()
        for i in range(25, 280, 10):
            pdf.line(13, i, 195, i)
        # set the footer
        pdf.ln(278)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='R')
        pdf.set_text_color(180, 180, 180)



pdf.output('output.pdf')