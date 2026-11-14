import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
text(ax,44,49,r'$\sqrt{x^2}=|x|$','resultat','l')
for y,a in ((26,r'$-5$'),(6,'5')):
    box(ax,2,y,16,12,role='sujet',label=a); arrow(ax,(20,y+6),(32,y+6),'varie'); text(ax,26,y+10,'carré','varie','s')
    box(ax,34,y,16,12,role='sujet',label='25'); arrow(ax,(52,y+6),(66,y+6),'varie'); text(ax,59,y+10,'racine','varie','s')
    box(ax,68,y,18,12,role='resultat',label='5')
save(fig,'22-054')
