import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,3,14,82,59,'fixe',fill=False,dash=True)
text(ax,52,69,'problème à 5 livres','fixe','s')
text(ax,13,66,'5 choix','varie','s')
for y,l in zip([55,46,37,28,19],'ABCDE'):
    box(ax,8,y,10,8,'varie',label=l)
    box(ax,21,y,60,8,'sujet',label='problème à 4 livres : 24',size='s')
    arrow(ax,(18.3,y+4),(20.7,y+4),'varie',lw=0.7)
text(ax,44,6,'5 × 4! = 5 × 24 = 120','resultat','l')
save(fig,'01-057')
