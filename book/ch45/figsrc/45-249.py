import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cs=[([0,3],'H','sujet'),([1,4],'1 + H','resultat'),([2,5],'2 + H','autre')]
xs=[14,44,74]
for (m,t,r),x in zip(cs,xs):
    box(ax,x-8,16,16,30,r,dash=True)
    disc(ax,x,38,4,r,label=str(m[0])); disc(ax,x,24,4,r,label=str(m[1]))
    text(ax,x,50,t,r,'m')
for a,b in [(0,1),(1,2)]:
    for y in (38,24): arrow(ax,(xs[a]+8.8,y),(xs[b]-8.8,y),'varie',lw=0.9)
text(ax,29,43,'+ 1','varie','s'); text(ax,59,43,'+ 1','varie','s')
text(ax,44,6,'3 classes × 2 éléments = 6','resultat','m')
save(fig,'45-249')
