import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
text(ax,44,79,'paquets de 4','encre','m')
for digits,x,y,role in [('1706',8,68,'fixe'),('106',15,50,'fixe'),('26',22,32,'fixe'),('2',29,14,'resultat')]:
    n=len(digits); w=7*n
    box(ax,x,y,w,7,role,fill=False)
    for i in range(1,n): line(ax,[(x+7*i,y),(x+7*i,y+7)],'fixe',lw=0.4)
    for i,d in enumerate(digits): text(ax,x+7*i+3.5,y+3.5,d,role,'l')
for (y0,y1,t,ty) in [(71.5,53.5,'− 400 × 4 = 1 600',62.5),(53.5,35.5,'− 20 × 4 = 80',44.5),(35.5,17.5,'− 6 × 4 = 24',26.5)]:
    arrow(ax,(37.5,y0),(37.5,y1),'varie',curve=-0.4)
    text(ax,43,ty,t,'varie','m',ha='left')
for y,t in [(71.5,'1 706 < 4 : faux'),(53.5,'106 < 4 : faux'),(35.5,'26 < 4 : faux')]:
    text(ax,84,y,t,'limite','s',ha='right')
text(ax,84,17.5,"2 < 4 : vrai, on s'arrête",'resultat','m',ha='right')
save(fig,'03-064')
