import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
u=17; x0=32
text(ax,3,53,'polynôme','encre','s',ha='left'); box(ax,x0,48,3*u,9,'sujet',label='degré 3',size='s')
text(ax,3,39,'cas 1','encre','s',ha='left'); box(ax,x0,34,u,9,'resultat',label='degré 1',size='s'); box(ax,x0+u,34,2*u,9,'fixe',label='degré 2',size='s')
text(ax,3,25,'cas 2','encre','s',ha='left')
for i in range(3): box(ax,x0+i*u,20,u,9,'resultat',label='degré 1',size='s')
text(ax,44,12,'toujours un facteur degré 1','resultat','s')
text(ax,44,5,'donc une racine rationnelle','resultat','s')
save(fig,'61-186')
