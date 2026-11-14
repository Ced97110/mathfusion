import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
rows=[48,32,16]
text(ax,14,61,r'$S$','sujet','l',weight='bold'); text(ax,74,61,r'$T$','autre','l',weight='bold')
for y,a,b in zip(rows,['1','2','3'],['a','b','c']):
    disc(ax,14,y,3.6,'sujet',label=a); disc(ax,74,y,3.6,'autre',label=b)
    arrow(ax,(18.6,y),(69.4,y),'fixe',curve=-0.12)
    arrow(ax,(69.4,y),(18.6,y),'sujet',curve=-0.12)
text(ax,44,54.5,r'$\alpha$','fixe','m'); text(ax,44,41.5,r'$\alpha^{-1}$','sujet','m')
text(ax,44,5,r'$\alpha^{-1}$ : l’inverse de $\alpha$','sujet','m')
save(fig,'42-241')
