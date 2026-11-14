import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,17,55,'nombre','fixe','s')
box(ax,34,50,22,10,'sujet',label='brique 1'); box(ax,60,50,24,10,'sujet',label='brique √2')
for y,lab,a,b in [(34,'3 + 5√2','3','5'),(18,'½ + √2','½','1')]:
    text(ax,17,y+5,lab,'encre','m')
    box(ax,34,y,22,10,'varie',label=a); box(ax,60,y,24,10,'varie',label=b)
box(ax,16,2,56,10,'resultat',label='[ℚ(√2) : ℚ] = 2')
save(fig,'61-046')
