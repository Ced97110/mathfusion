import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,"ensemble : pas d'ordre",'fixe','s')
box(ax,4,44,32,12,'fixe',label=r'$\{2,5\}$'); box(ax,52,44,32,12,'fixe',label=r'$\{5,2\}$')
line(ax,[(40,51),(48,51)],'resultat',lw=1.2); line(ax,[(40,49),(48,49)],'resultat',lw=1.2)
text(ax,44,34,"couple : l'ordre compte",'sujet','s')
for x,(a,b) in ((4,('2','5')),(52,('5','2'))):
    box(ax,x,12,14,12,'sujet',label=a); box(ax,x+16,12,14,12,'sujet',label=b)
text(ax,44,18,r'$\neq$','limite','xl')
text(ax,11,7,'1re place','sujet','s'); text(ax,27,7,'2e place','sujet','s')
save(fig,'42-159')
