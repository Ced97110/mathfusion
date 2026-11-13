import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=2.4; X=46
text(ax,44,60,r'$2\times3\times5\times7+1=211$','encre','m')
line(ax,[(X,12),(X,54)],'fixe',dash=True)
for i,(p,q) in enumerate([(2,105),(3,70),(5,42),(7,30)]):
    y=44-i*8.5
    for b in range(2):
        xa=X-(b+1)*p*u
        box(ax,xa,y-3,p*u,6,'sujet',r=0.3,lw=0.6)
    xl=X-2*p*u
    text(ax,xl-2.2,y,'…','sujet','s')
    box(ax,X,y-3,u,6,'varie',r=0.3,lw=0.6)
    text(ax,53,y,r'$211=%d\times%d+1$'%(p,q),'encre','s',ha='left')
text(ax,X-0.6,7,'210','sujet','s',ha='right')
text(ax,X+0.6,7,'211','varie','s',ha='left')
text(ax,70,7,'reste 1','varie','s')
save(fig,'05-163')
