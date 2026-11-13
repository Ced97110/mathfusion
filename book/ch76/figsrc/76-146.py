import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66); O=(6,36); s=6
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
poly(ax,[P(0,0),P(3,1),P(4,3),P(1,2)],'sujet')
arrow(ax,P(0,0),P(3,1),'sujet',lw=1.2); arrow(ax,P(0,0),P(1,2),'sujet',lw=1.2)
text(ax,P(2,1.5)[0],P(2,1.5)[1],'aire 5','sujet','m')
text(ax,19,57,r'$u=(3,1)$, $v=(1,2)$','sujet','s')
for i in range(5): poly(ax,[(44+i*8,38),(44+i*8+6,38),(44+i*8+6,44),(44+i*8,44)],'autre')
text(ax,62,32,r'$5\,e_{12}$','autre','m')
arrow(ax,(32,42),(42,42),'varie'); text(ax,37,47,r'$u\wedge v$','varie','s')
box(ax,34,4,20,9,'resultat',label='5',size='l')
arrow(ax,(16,34),(35,14),'resultat',curve=0.0); text(ax,16,22,r'$B$','resultat','m')
arrow(ax,(62,29),(50,14),'resultat'); text(ax,63,19,r'$\tilde{B}$ : $e_{12}\mapsto 1$','resultat','s',ha='left')
save(fig,'76-146')
