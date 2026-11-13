import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,22,62,'sous-monoïde','autre','m'); text(ax,66,62,'quotient','sujet','m')
xs=[6+i*32/7 for i in range(8)]
for i,x in enumerate(xs): disc(ax,x,40,1.8,'fixe' if i<3 else 'autre')
brace(ax,xs[0]-2,xs[2]+2,36,'fixe','négatifs'); brace(ax,xs[3]-2,xs[7]+2,36,'autre','positifs')
text(ax,22,18,'on choisit des éléments','autre','s')
for k,x in enumerate([46,59.5,73]):
    box(ax,x,32,11,20,'sujet'); text(ax,x+5.5,27,f'classe {k}','sujet','s')
    for j in range(3): disc(ax,x+5.5,37+j*5,1.8,'sujet',fill=False)
text(ax,66,18,'on rassemble en paquets','sujet','s')
save(fig,'47-111')
