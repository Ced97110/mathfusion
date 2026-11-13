import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
s=6
for i in range(5):
    for j in range(5): box(ax,6+i*s,14+j*s,s,s,'sujet',lw=0.5,r=0.2)
text(ax,21,50,'aire $25$','sujet','m')
f=numberline(ax,52,82,29,0,5,arrow_right=False,every=5)
line(ax,[(f(0),29),(f(5),29)],'resultat',lw=2.4)
arrow(ax,(38,29),(50,29),'varie')
text(ax,44,34,'$\\sqrt{25}$','varie','s')
text(ax,67,36,'côté','resultat','m')
text(ax,67,18,'$\\sqrt{25}=5$','resultat','m')
save(fig,'22-132')
