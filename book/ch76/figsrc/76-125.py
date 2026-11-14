import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=5
def par(o,A,B,role):
    pts=[(0,0),A,(A[0]+B[0],A[1]+B[1]),B]
    for i in range(int(max(p[0] for p in pts))+1):
        for j in range(int(max(p[1] for p in pts))+1): disc(ax,o[0]+i*u,o[1]+j*u,0.45,'fixe')
    poly(ax,[(o[0]+x*u,o[1]+y*u) for x,y in pts],role)
par((4,32),(2,1),(1,1),'sujet'); par((26,32),(3,1),(2,1),'autre')
text(ax,13,22,r'$\det X=1$','sujet','m'); text(ax,38,22,r'$\det Y=1$','autre','m')
box(ax,58,30,26,18,'resultat'); text(ax,71,42,r'$7\quad 5$','resultat','m'); text(ax,71,35,r'$4\quad 3$','resultat','m')
text(ax,71,24,r'$\det XY=1$','resultat','m')
text(ax,44,58,r'$1\times1=1$','resultat','l')
text(ax,44,8,'tout reste entier','fixe','m')
save(fig,'76-125')
