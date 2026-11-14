import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
box(ax,6,58,76,13,'sujet')
text(ax,44,67,'un quotient exige','sujet','m',weight='bold')
text(ax,44,61.5,'un sous-groupe normal','sujet','m',weight='bold')
arrow(ax,(44,58),(44,55.5),'sujet')
specs=[(4,'reste 1','sujet',['5','9']),(32,'reste 2','varie',['6','10']),(60,'reste 3','resultat',['11','19'])]
for x,t,r,ns in specs:
    box(ax,x,18,24,34,r)
    text(ax,x+12,47,t,r,'s')
    for i,n in enumerate(ns): text(ax,x+12,37-i*9,n,r,'l')
text(ax,30,34,'+','encre','l'); text(ax,58,34,'=','encre','l')
text(ax,44,9,'19 − 11 = 8 = 2 × 4','resultat','m')
save(fig,'52-001')
