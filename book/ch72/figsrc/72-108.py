import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
cx,cy,u=24,36,12
line(ax,[(6,cy),(80,cy)],'fixe',lw=1.2); line(ax,[(cx,cy-16),(cx,cy+20)],'fixe',lw=0.6)
arrow(ax,(cx,cy),(cx,cy+u),'fixe'); arrow(ax,(cx,cy),(cx+2*u,cy+u),'sujet'); arrow(ax,(cx,cy),(cx+2*u,cy-u),'resultat')
arrow(ax,(cx+2*u,cy+u-1.5),(cx+2*u,cy-u+1.5),'varie',lw=0.8)
text(ax,cx-2,cy+u,r'$e_2$','fixe','m',ha='right')
text(ax,cx+2*u+3,cy+u+2,r'$x=(2,1)$','sujet','s',ha='left'); text(ax,cx+2*u+3,cy-u-2,r'$S_{e_2}x=(2,-1)$','resultat','s',ha='left')
text(ax,68,cy+3,'axe horizontal','fixe','s')
text(ax,6,62,r'$e_2=(0,1)$ : carré $-1$','fixe','s',ha='left')
text(ax,44,8,r'$(x_1,x_2)\to(x_1,-x_2)$','resultat','m')
save(fig,'72-108')
