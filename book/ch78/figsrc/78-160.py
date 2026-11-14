import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
f=numberline(ax,8,72,30,1,9,1)
for d in range(1,10):
    r='resultat' if d==1 else ('limite' if d%2 else 'fixe')
    disc(ax,f(d),39,3.4,r)
text(ax,44,53,'dimension de l’algèbre','encre','s')
for x,r,s in [(4,'resultat','1 : les réels'),(30,'limite','impair > 1 : exclu'),(60,'fixe','pair : non traité')]:
    pass
disc(ax,6,6,2,'resultat'); text(ax,9,6,'1 : réels','resultat','s',ha='left')
disc(ax,36,6,2,'limite'); text(ax,39,6,'impair > 1 : exclu','limite','s',ha='left')
disc(ax,6,15,2,'fixe'); text(ax,9,15,'pair : non traité ici','fixe','s',ha='left')
save(fig,'78-160')
