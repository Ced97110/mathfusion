import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(64)
box(ax,2,50,26,9,'fixe',label='$z=3+4i$',size='s')
box(ax,31,50,26,9,'sujet',label='$T=2\\times3=6$',size='s')
box(ax,60,50,26,9,'varie',label='$N=9+16=25$',size='s')
xs=[2,31,60]; rs=['fixe','sujet','varie']
sym=['$\\lambda^2$','$-T\\lambda$','$+N$']; num=['$\\lambda^2$','$-6\\lambda$','$+25$']
for x,r,a,b in zip(xs,rs,sym,num):
    box(ax,x,28,26,9,r,label=a)
    box(ax,x,8,26,9,r,label=b)
arrow(ax,(44,50),(44,38),'sujet'); arrow(ax,(73,50),(73,38),'varie'); arrow(ax,(15,50),(15,38),'fixe')
for x,r in zip([15,44,73],rs): arrow(ax,(x,28),(x,18),r)
text(ax,44,22.5,'on remplace','fixe','s') if False else None
save(fig,'77-073')
