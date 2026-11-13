import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,r'$HN$ : 4 produits $hn$','sujet','m',weight='bold')
cells=[(2,36,'id','sujet'),(31,36,r'$1\leftrightarrow2$','sujet'),(60,36,r'$1\leftrightarrow3$','sujet'),
       (2,18,r'$1\to3\to2\to1$','sujet'),(31,18,r'$2\leftrightarrow3$','fixe'),(60,18,r'$1\to2\to3\to1$','limite')]
for x,y,l,r in cells: box(ax,x,y,26,12,r,label=l,size='s',dash=(r=='limite'))
text(ax,44,12,'pas un produit','fixe','s')
text(ax,73,12,'nh : hors de HN','limite','s')
save(fig,'48-121')
