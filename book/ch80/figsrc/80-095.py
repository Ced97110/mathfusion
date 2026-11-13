import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(66)
text(ax,44,60,'2 + 2 − 3 = 1','resultat','xl')
box(ax,43,14,19,40,'varie',fill=False,dash=True)
xs=[26,44,62]
for i,l in enumerate(['a','b']): box(ax,xs[i],42,17,8,'sujet',label=l,size='m')
for i,l in enumerate(['b','c']): box(ax,xs[i+1],30,17,8,'autre',label=l,size='m')
for i,l in enumerate(['a','b','c']): box(ax,xs[i],17,17,8,'resultat',label=l,size='m')
text(ax,2,46,'U : 2','sujet','m',ha='left')
text(ax,2,34,'W : 2','autre','m',ha='left')
text(ax,2,21,'U + W : 3','resultat','m',ha='left')
text(ax,52,9,'commun : 1','varie','s')
save(fig,'80-095')
