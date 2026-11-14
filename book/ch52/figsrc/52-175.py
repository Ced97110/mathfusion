import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,22,59,'noyau : multiples de 6','sujet','s')
box(ax,3,36,34,10,'resultat',label='12 → (0, 0)',size='s')
box(ax,3,14,34,10,'limite',label='3 → (1, 0)',size='s')
text(ax,20,29,'impair','limite','s')
cw,ch=14,12; ox,oy=50,22
text(ax,67,59,'2 × 3 = 6 paires','autre','s')
for r in range(2):
    for c in range(3):
        role='resultat' if (r,c)==(0,0) else 'autre'
        box(ax,ox+c*cw-8,oy+(1-r)*ch+0.0,cw-1,ch-1,role,label=f'({r}, {c})',size='s')
arrow(ax,(37,41),(ox-8+6.5-6.5,oy+ch+ch/2-0.5),'resultat')
arrow(ax,(37,19),(ox-8+0.0,oy+ch/2-0.5),'limite')
text(ax,67,15,'image : au plus 6 éléments','autre','s')
save(fig,'52-175')
