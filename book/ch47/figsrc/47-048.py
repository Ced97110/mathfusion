import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,67,r'$G/N$ : $12\div 4=3$ lignes','encre','m')
labs=[('ligne de 0 : 0 3 6 9','sujet'),('ligne de 1 : 1 4 7 10','sujet'),('ligne de 2 : 2 5 8 11','sujet')]
ys=[44,26,8]
for (l,r),y in zip(labs,ys): box(ax,3,y,54,13,r,label=l,size='s')
arrow(ax,(58,ys[1]+6.5),(58,ys[0]+6.5),'varie',curve=0.0) if False else None
arrow(ax,(58,ys[1]+8),(58,ys[0]+4),'varie',curve=-0.5)
arrow(ax,(58,ys[2]+8),(58,ys[0]+3),'varie',curve=-0.5)
text(ax,72,38,'1 + 2 = 3','varie','s'); text(ax,72,31,'ligne de 0','resultat','s')
save(fig,'47-048')
