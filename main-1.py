from reportlab.platypus import SimpleDocTemplate,Table,TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os,webbrowser
pdfmetrics.registerFont(TTFont("fz", "STFANGSO.TTF"))
doc = SimpleDocTemplate("Tabal4.pdf", )
content = []
data=[["词语","form"],
        ["翻译","表单",],
        ["词性",".n"]
       ]
t = Table(data,colWidths=150, rowHeights=150)
t.setStyle(TableStyle([("TEXTCOLOR",(0,0),(2,1),colors.red),
                        ("TEXTCOLOR",(1,1),(1,1),colors.blue),
                        ("INNERGRID",(0,0),(-1,-1),0.25,colors.black),
                        ("BOX",(0,0),(-1,-1),0.25,colors.black),
                        ("FONTSIZE",(0,0),(-1,-1),20),
                        ("FONTNAME",(0,0),(-1,-1),"fz"),
                        ("ALIGN",(0,0),(-1,-1),"CENTER"),
                        ("VALIGN",(0,0),(-1,-1),"MIDDLE")]))
content.append(t)
doc.build(content)
webbrowser.open('file://'+os.path.realpath("Tabal4.pdf"))
