import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,3,50,'mètres','sujet','s',ha='left'); text(ax,3,22,'centimètres','resultat','s',ha='left')
x0=30;c=9
for i,d in enumerate('235'):
    box(ax,x0+i*c,44,c-1,12,'sujet',label=d,size='l'); box(ax,x0+i*c,16,c-1,12,'resultat',label=d,size='l')
disc(ax,x0+c-0.5,44.5,1.2,'varie'); text(ax,x0+c-0.5,59,'2,35 m','sujet','s')
disc(ax,x0+3*c-1.0,16.5,1.2,'varie')
arrow(ax,(x0+c-0.5,38),(x0+3*c-1.0,32),'varie'); text(ax,x0+3*c+8,35,'× 100','varie','m',ha='left')
text(ax,x0+3*c/2-1,8,'235 cm : virgule 2 rangs à droite','varie','s')
save(fig,'08-094')
