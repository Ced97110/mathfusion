import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,58,r'$S_3$ : 6 façons de ranger les 3 droites','encre','s')
P=[(19,43),(9,22),(29,22)]
for i,j in [(0,1),(1,2),(0,2)]: line(ax,[P[i],P[j]],'fixe')
for k,(x,y) in enumerate(P): disc(ax,x,y,4,'sujet',label=str(k+1))
text(ax,19,12,'les 3 droites','sujet','s')
box(ax,38,29,49,16,'resultat',fill=False,dash=True,lw=1.0)
for k,l in enumerate(['123','231','312']): box(ax,40+15*k,31,13,9,'resultat',label=l,size='s')
text(ax,62,48,r'$A_3$ : 3 façons, sous-groupe normal','resultat','s')
for k,l in enumerate(['132','213','321']): box(ax,40+15*k,14,13,9,'varie',label=l,size='s')
text(ax,62,9,'3 échanges de deux droites','varie','s')
text(ax,62,3.5,r'3 + 3 = 6 : $S_3$ contient $A_3$ : pas simple','encre','s')
[p.set_zorder(3.5) for p in ax.patches if isinstance(p,Circle)]
save(fig,'73-179')
