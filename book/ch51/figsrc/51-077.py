import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
ox,oy,L=10,12,40
arrow(ax,(ox,oy),(ox+L+6,oy),'fixe',lw=0.8); arrow(ax,(ox,oy),(ox,oy+L+6),'fixe',lw=0.8)
line(ax,[(ox,oy),(ox+L,oy+L)],'sujet',lw=1.3); line(ax,[(ox,oy+L),(ox+L,oy)],'varie',lw=1.3)
for v,t in [(0,'0'),(1,'1')]: text(ax,ox+v*L,oy-3.5,t,'fixe','s')
text(ax,ox+L/2,oy-3.5,r'$\frac{1}{2}$','fixe','s')
text(ax,ox+L-2,oy+L-6.5,r'$f$','sujet','m'); text(ax,ox+4,oy+L-8,r'$g$','varie','m')
line(ax,[(ox+L/2,oy),(ox+L/2,oy+L)],'fixe',dash=True,lw=0.6)
disc(ax,ox+L/2,oy+L/2,1.4,'fixe'); disc(ax,ox+L/2,oy+L,1.4,'resultat'); disc(ax,ox+L/2,oy+L/4,1.4,'resultat')
for y,s,r in [(oy+L,r'somme $=1$','resultat'),(oy+L/4,r'produit $=\frac{1}{4}$','resultat'),(oy+L/2,r'$f$ et $g$ valent $\frac{1}{2}$','fixe')]:
    line(ax,[(ox+L/2+2,y),(ox+L+8,y)],r,dash=True,lw=0.6)
    text(ax,ox+L+9,y,s,r,'s',ha='left') if r=='resultat' else text(ax,ox+L+9,y+3.5,s,r,'s',ha='left')
save(fig,'51-077')
