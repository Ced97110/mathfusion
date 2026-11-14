import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,22,54,r'$|-5|=5$','autre','xl'); text(ax,66,54,r'$|D_4|=8$','sujet','xl')
text(ax,22,47,'un nombre dedans','autre','s'); text(ax,66,47,'un groupe dedans','sujet','s')
f=numberline(ax,6,38,28,-5,0,labels=False,arrow_right=False)
disc(ax,f(-5),28,1.4,'autre'); disc(ax,f(0),28,1.4,'fixe')
text(ax,f(-5),23,r'$-5$','autre','s'); text(ax,f(0),23,r'$0$','fixe','s')
brace(ax,f(-5),f(0),19,'autre',label='distance 5')
box(ax,48,14,36,28,'sujet')
for r in range(2):
    for c in range(4): disc(ax,55+8.2*c,34-9*r,3,'sujet')
text(ax,22,6,'valeur absolue','autre','s'); text(ax,66,6,'ordre : nombre d’éléments','sujet','s')
save(fig,'47-053')
