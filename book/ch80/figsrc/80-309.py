import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
O=(14,10); s=3.4
for r,tip,v in [('sujet',(0,4),(0,1)),('autre',(4,8),(1,2)),('varie',(4,12),(1,3))]:
    q=(O[0]+s*tip[0],O[1]+s*tip[1])
    line(ax,[O,(O[0]+1.2*s*tip[0],O[1]+1.2*s*tip[1])],'fixe',0.5)
    arrow(ax,O,q,r,1.5)
    arrow(ax,O,(O[0]+s*v[0],O[1]+s*v[1]),'fixe',1.0)
text(ax,6,24,'(0, 4)','sujet','s'); text(ax,36,38,'(4, 8)','autre','s'); text(ax,37,52,'(4, 12)','varie','s')
text(ax,24,66,r'exemple : $\lambda=4$','encre','s')
box(ax,46,54,40,10,'fixe',label=r'$\eta$ fixe les pentes $\infty$, 2, 3',size='s')
box(ax,46,38,40,10,'varie',label=r'test pente 3 : $c=\lambda$',size='s')
box(ax,46,22,40,10,'resultat',label=r'donc $\eta$ = multiplication par $\lambda$',size='s')
arrow(ax,(66,53.5),(66,48.5),'fixe',0.9); arrow(ax,(66,37.5),(66,32.5),'fixe',0.9)
text(ax,66,14,r'$\eta(0,1)=c\,(0,1)$','fixe','s'); text(ax,66,7,r'$\eta(1,2)=\lambda\,(1,2)$','fixe','s')
save(fig,'80-309')
