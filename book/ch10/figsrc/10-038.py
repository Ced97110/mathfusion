import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,15,68,'nombre vrai','fixe','s'); text(ax,73,68,'nombre remplacé','fixe','s')
for y,a,b,d in((53,'2 357','2 400','+43'),(39,'6 106','6 100','−6')):
    box(ax,2,y,26,9,'sujet',label=a); box(ax,62,y,24,9,'varie',label=b)
    arrow(ax,(31,y+4.5),(59,y+4.5),'varie'); text(ax,45,y+8,d,'varie','s')
line(ax,[(2,34),(86,34)],'fixe',dash=True)
box(ax,2,20,26,9,'sujet',label='8 463'); box(ax,62,20,24,9,'varie',label='8 500')
arrow(ax,(31,24.5),(59,24.5),'varie',lw=1.8); text(ax,45,28,'+37','varie','s')
box(ax,14,4,60,9,'resultat',label='37 = 43 − 6')
save(fig,'10-038')
