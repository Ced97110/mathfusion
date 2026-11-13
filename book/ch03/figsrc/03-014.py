import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig,ax=canvas(70)
text(ax,3,62,r'1. lire $a$ = 4','varie','s',ha='left')
for x in (40,52,64,76):
    disc(ax,x,62,1.3,'varie')
    line(ax,[(x,60.7),(x,51)],'fixe',lw=0.5,dash=True)
text(ax,3,48,r'2. écrire $b$, 4 fois','autre','s',ha='left')
for x in (36,48,60,72):
    box(ax,x,45,8,6,'autre',label='6',size='m')
text(ax,3,27,'3. additionner','varie','s',ha='left')
f=numberline(ax,34,82,24,0,24,step=6,arrow_right=False)
for a,b in ((0,6),(6,12),(12,18),(18,24)):
    arrow(ax,(f(a),25.5),(f(b),25.5),'varie',lw=0.9,curve=-0.5)
    m=(f(a)+f(b))/2
    line(ax,[(m,45),(m,28.6)],'fixe',lw=0.5,dash=True)
disc(ax,82,24,1.4,'resultat')
text(ax,58,10,'4 × 6 = 24','resultat','l')
save(fig,'03-014')
