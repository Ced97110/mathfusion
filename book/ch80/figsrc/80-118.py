import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
o=iso(0,0,0,(22,18),1); u=17
for (x,y,z,l,r) in [(1,0,0,r'$e_1$','sujet'),(0,1,0,r'$e_2$','varie'),(0,0,1,r'$e_3$','resultat')]:
    p=iso(x,y,z,(22,18),u); arrow(ax,(22,18),p,r,lw=1.2); text(ax,p[0]+(3 if x else -3 if y else 0),p[1]+(0 if z==0 else 3),l,r,'m')
text(ax,22,62,'3 directions : espace','resultat','s')
arrow(ax,(66,18),(84,18),'sujet',lw=1.2); arrow(ax,(66,18),(78,34),'varie',lw=1.2)
text(ax,85,13,r'$e_1$','sujet','m',ha='right'); text(ax,80,38,r'$e_2$','varie','m')
text(ax,70,62,'plan : tout est dedans','limite','s')
box(ax,56,44,30,8,'limite',label=r'pas de $e_3$',size='s',dash=True)
save(fig,'80-118')
