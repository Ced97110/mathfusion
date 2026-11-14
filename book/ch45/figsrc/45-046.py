import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(75)
xs=[14,34,54,74]
for k,x,p,r in zip(range(4),xs,[1,2,4,8],[1,2,4,3]):
    text(ax,x,68,rf'$k={k}$','sujet','m')
    hl=(k==3)
    box(ax,x-8.5,42,17,10,'varie' if hl else 'fixe',label=rf'$2^{k}={p}$',size='s')
    arrow(ax,(x,41),(x,29),'varie' if hl else 'fixe')
    box(ax,x-6,16,12,10,'varie' if hl else 'resultat',label=str(r),size='l')
arrow(ax,(x,60.5),(x,53.5),'fixe') if False else None
for x in xs: arrow(ax,(x,64),(x,53.5),'fixe')
text(ax,44,6,'restes de la division par 5','resultat','s')
save(fig,'45-046')
