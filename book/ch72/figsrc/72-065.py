import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(66); ox,oy,u=26,32,22
line(ax,[(4,oy),(72,oy)]); line(ax,[(ox,6),(ox,60)])
th=[2*math.pi*i/90 for i in range(91)]
line(ax,[(ox+u*math.cos(t),oy+u*math.sin(t)) for t in th],'fixe',dash=True)
line(ax,[(ox+u*math.cosh(t/30),oy+u*math.sinh(t/30)) for t in range(-30,31)],'resultat',lw=1.2)
p=(ox+u,oy); q=(ox+u*5/4,oy+u*3/4)
disc(ax,*p,1.3,'sujet'); disc(ax,*q,1.3,'resultat')
arrow(ax,(p[0]+1,p[1]+1),(q[0]-0.5,q[1]-1.5),'varie',curve=-0.3)
text(ax,p[0]+4,p[1]-4,'(1, 0)','sujet','s')
text(ax,q[0]+3,q[1]-5,'(5/4, 3/4)','resultat','s',ha='left')
text(ax,ox-14,oy+22,'cercle : carré 1','fixe','s')
text(ax,72,57,'hyperbole','resultat','s'); text(ax,72,53,'carré 1','resultat','s')
text(ax,44,6,'le point sort du cercle','varie','s'); 
save(fig,'72-065')
