import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
text(ax,44,62,r'0 ÷ 7 : 7 $\times$ $q$ = 0 ?','sujet','l')
text(ax,16,53,'7 rangées','fixe','s')
for x in (10,38,66):
    for j in range(7): disc(ax,x,21.5+3*j,0.6,'fixe')
for j in range(7): box(ax,13,20+3*j,6,3,'fixe',fill=False,dash=True,r=0.3,lw=0.5)
for j in range(7): box(ax,41,20+3*j,3,3,'limite',r=0.3,lw=0.5)
for i in range(2):
    for j in range(7): box(ax,69+3*i,20+3*j,3,3,'limite',r=0.3,lw=0.5)
for x,q,t,r in ((16,0,r'7 $\times$ 0 = 0','resultat'),(44,1,r'7 $\times$ 1 = 7','limite'),(72,2,r'7 $\times$ 2 = 14','limite')):
    text(ax,x,47,rf'$q$ = {q}','varie','s'); text(ax,x,15,t,r,'s')
text(ax,44,6,r'seul $q$ = 0 donne 0','resultat','m')
save(fig,'03-109')
