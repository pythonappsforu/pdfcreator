from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P',unit='mm',format='a4')
df = pd.read_csv('topics.csv')
for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(10,1,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)
    pdf.line(13,25,195,25)
    no_of_pages = row['Pages']
    while no_of_pages > 1:
        pdf.add_page()
        no_of_pages -= 1


pdf.output('output.pdf')