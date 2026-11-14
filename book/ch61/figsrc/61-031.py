import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,19,46,'coefficient dans $K$','varie','s')
text(ax,48,46,'brique','sujet','s')
rows=[('2+√2','1',28),('5+3√2','√3',10)]
for c,b,y in rows:
    box(ax,4,y,30,9,'varie',label=c)
    text(ax,38,y+4.5,'×','encre','m')
    box(ax,42,y,12,9,'sujet',label=b)
    arrow(ax,(54,y+4.5),(65,28 if y>20 else 24),'resultat')
text(ax,19,23.5,'+','encre','m')
box(ax,66,19,20,14,'resultat',label='nombre\nde $E$')
save(fig,'61-031')
