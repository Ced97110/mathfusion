import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
C=[15,44,73]
heads=[r'$(a+b)^2$',r'$(a-b)^2$',r'$(a+b)(a-b)$']; mids=[(r'$+ab$',r'$+ab$'),(r'$-ab$',r'$-ab$'),(r'$-ab$',r'$+ab$')]
res=[('+2ab','resultat'),('−2ab','resultat'),('aucun','fixe')]
for c,h,(m1,m2),(rt,rr) in zip(C,heads,mids,res):
    text(ax,c,54,h,'sujet','s')
    box(ax,c-11,39,10.5,8,'sujet'); box(ax,c+0.5,39,10.5,8,'varie',label=m1,size='s')
    box(ax,c-11,30,10.5,8,'varie',label=m2,size='s'); box(ax,c+0.5,30,10.5,8,'autre')
    arrow(ax,(c,28),(c,23),'fixe'); box(ax,c-12,13,24,9,rr,label=rt,dash=(rr=='fixe'))
text(ax,C[0]-5.7,43,r'$a^2$','sujet','s'); text(ax,C[0]+5.7,34,r'$b^2$','autre','s')
save(fig,'15-110')
