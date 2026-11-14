import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52); s=7; O=(8,12)
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
line(ax,[P(0,0),P(9,3)],'fixe',dash=True)
arrow(ax,P(0,0),P(6,2),'autre',lw=1.2)
arrow(ax,P(0,0),P(3,1),'sujet',lw=2.2)
for (a,b,r) in [(0,0,'fixe'),(3,1,'sujet'),(6,2,'autre'),(9,3,'fixe')]:
    disc(ax,*P(a,b),0.9,r)
q=P(3,1); text(ax,q[0],q[1]-4,r'$u$','sujet','m')
q=P(6,2); text(ax,q[0],q[1]-4,r'$v=2u$','autre','m')
q=P(9,3); text(ax,q[0]-2,q[1]+4,r'$u+v$','fixe','m')
text(ax,44,46,r'$u\wedge v=0$','resultat','l')
text(ax,44,39,'parallélogramme aplati','resultat','s')
save(fig,'76-129')
