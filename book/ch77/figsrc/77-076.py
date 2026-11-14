import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax,x,y,cw,ch,rows,roles,size="m"):
    for i,r in enumerate(rows):
        for j,v in enumerate(r):
            box(ax,x+j*cw+0.25,y+(len(rows)-1-i)*ch+0.25,cw-0.5,ch-0.5,roles[i][j],label=v,size=size)

fig,ax=canvas(80)
box(ax,2,66,28,10,'sujet',label='$z=2+i$',size='m')
arrow(ax,(31,71),(54,71),'varie'); text(ax,42.5,74.5,'au carré','varie','s')
box(ax,56,66,30,10,'varie',label='$z^2=3+4i$',size='m')
box(ax,2,52,28,8,'sujet',label='$N=5$',size='m')
box(ax,56,52,30,8,'varie',label='$N=25=5^2$',size='s')
u=8.5; O=(14,8)
poly(ax,[O,(O[0]+4*u,O[1]),(O[0]+4*u,O[1]+3*u)],'resultat')
text(ax,O[0]+2*u,O[1]-0.0+2.6,'4','resultat','m')
text(ax,O[0]+4*u+3,O[1]+1.5*u,'3','resultat','m')
text(ax,O[0]+2*u-5,O[1]+1.8*u+2,'5','resultat','m')
text(ax,66,24,'$3^2+4^2=5^2$','resultat','m')
save(fig,'77-076')
