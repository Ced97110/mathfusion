import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
ox,oy,u=14,36,6
arrow(ax,(4,oy),(80,oy),'fixe',lw=0.8); arrow(ax,(ox,6),(ox,67),'fixe',lw=0.8)
text(ax,81,oy+3,'réel','fixe','s',ha='right'); text(ax,ox+2,65,'en $i$','fixe','s',ha='left')
line(ax,[(ox+3*u,oy+4*u),(ox+3*u,oy-4*u)],'varie',dash=True)
disc(ax,ox+3*u,oy+4*u,1.6,'sujet'); disc(ax,ox+3*u,oy-4*u,1.6,'autre')
text(ax,ox+3*u+3,oy+4*u,'$3+4i$','sujet','m',ha='left')
text(ax,ox+3*u+3,oy-4*u,'$3-4i$','autre','m',ha='left')
text(ax,ox+3*u,oy-3.5,'3','fixe','s')
text(ax,ox+3*u+3,oy-11,'signe de la\npartie en $i$ changé','varie','s',ha='left')
save(fig,'51-183')
