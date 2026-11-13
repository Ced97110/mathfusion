import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
u=10; ox,oy=8,12; b=0.5
for k in range(5): line(ax,[(ox+k*u,oy),(ox+k*u,oy+3*u)],'fixe',lw=0.4)
for k in range(1,4): line(ax,[(ox,oy+k*u),(ox+4*u,oy+k*u)],'fixe',lw=0.4)
line(ax,[(ox,oy),(ox+4*u,oy)],'fixe',lw=1.8)
for k in range(5): line(ax,[(ox+k*u,oy),(ox+(k+3*b)*u,oy+3*u)],'sujet',lw=0.8)
for k in range(1,4): line(ax,[(ox+k*b*u,oy+k*u),(ox+(4+k*b)*u,oy+k*u)],'sujet',lw=0.8)
for k,lab in [(1,'+1/2'),(2,'+1'),(3,'+3/2')]:
    arrow(ax,(ox+4*u,oy+k*u),(ox+(4+k*b)*u,oy+k*u),'varie',lw=1.3)
    text(ax,ox+(4+k*b)*u+2,oy+k*u,lab,'varie','s',ha='left')
arrow(ax,(ox+u+1.5,oy+2*u),(ox+2*u-1.5,oy+2*u),'varie',lw=1.3)
disc(ax,ox+u,oy+2*u,1.2,'varie'); disc(ax,ox+2*u,oy+2*u,1.2,'resultat')
text(ax,ox+u-3,oy+2*u+3.5,r'$P$','varie','s'); text(ax,ox+2*u+3,oy+2*u+3.5,r"$P'$",'resultat','s')
text(ax,ox,oy-4,r'$D$ : ne bouge pas','fixe','s',ha='left')
save(fig,'73-011')
