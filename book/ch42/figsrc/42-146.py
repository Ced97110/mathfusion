import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[14,30,46]; roles=['sujet','autre','fixe']
for x,l,r in zip(xs,'ABC',roles): text(ax,x,54,l,r,'l')
for y,g,lab in ((40,(7,30),r'$(A\cup B)\cup C$'),(18,(23,30),r'$A\cup(B\cup C)$')):
    box(ax,g[0],y-6,g[1],12,'varie',fill=False,dash=True)
    for x,n,r in zip(xs,'123',roles): disc(ax,x,y,3,r,label=n)
    text(ax,g[0]+g[1]/2,y-9,lab,'varie','s')
box(ax,62,20,24,22,'resultat',label=r'$\{1,2,3\}$')
arrow(ax,(52,40),(62,36),'resultat'); arrow(ax,(55,18),(62,26),'resultat')
save(fig,'42-146')
