import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,44,62,r'$F(m)$ = $E(3+m)$','autre','m')
X=[10,34,58]
for i,x in enumerate(X):
    box(ax,x,46,16,10,'autre',label=rf'$F({i})$')
    box(ax,x,18,16,10,'sujet',label=rf'$E({3+i})$')
box(ax,10,46,16,10,'resultat',fill=False,lw=1.6)
box(ax,10,18,16,10,'resultat',fill=False,lw=1.6)
for x in [18,42,66]:
    line(ax,[(x-0.5,29),(x-0.5,45)],'fixe'); line(ax,[(x+0.5,29),(x+0.5,45)],'fixe')
text(ax,9.5,37,'départ','resultat','s')
for y in (51,23):
    arrow(ax,(26,y),(34,y),'varie'); arrow(ax,(50,y),(58,y),'varie')
    line(ax,[(74,y),(85,y)],'varie',dash=True)
text(ax,54,37,'même passage','varie','s')
brace(ax,10,84,15,'resultat',label=r'$E(n)$ vraie pour $n \geq 3$',size='m')
save(fig,'01-139')
