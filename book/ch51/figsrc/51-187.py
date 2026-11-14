import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
cw,ch=20,9; x0=24
text(ax,44,84,'déterminant du tableau','encre','s')
ent=[[('$1+2i$','sujet'),('$2i$','varie')],[('$2i$','varie'),('$1-2i$','sujet')]]
for r in range(2):
    for c in range(2):
        l,ro=ent[r][c]; box(ax,x0+c*cw,62+(1-r)*ch,cw,ch,ro,label=l,r=0.2)
for x,d in ((x0-1.5,1),(x0+2*cw+1.5,-1)):
    line(ax,[(x+d*1.5,61.5),(x,61.5),(x,80.5),(x+d*1.5,80.5)],'encre')
arrow(ax,(44,60),(44,48),'fixe'); text(ax,48,54,'carrés des coordonnées','fixe','s',ha='left')
u=4.5; yb=36
for k,(xc,sd,ro) in enumerate(zip((13,33,53,73),(1,2,0,2),('sujet','sujet','varie','varie'))):
    if sd: box(ax,xc-sd*u/2,yb,sd*u,sd*u,ro,r=0.05)
    else: disc(ax,xc,yb+0.7,0.7,ro)
    text(ax,xc,yb-3.5,r'$\alpha_%d^2=%d$'%(k,sd*sd),ro,'s')
brace(ax,5,41,29,'sujet',label=r'$a\bar{a}=5$'); brace(ax,45,81,29,'varie',label=r'$b\bar{b}=4$')
text(ax,44,12,r'déterminant $=5+4=9$','resultat','m')
save(fig,'51-187')
