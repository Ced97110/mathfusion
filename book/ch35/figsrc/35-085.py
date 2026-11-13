import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,r=30,32,22
disc(ax,cx,cy,r,'sujet')
line(ax,[(4,cy),(56,cy)],'fixe',lw=0.6); line(ax,[(cx,cy-r-2),(cx,cy+r+8)],'fixe',lw=0.6)
line(ax,[(4,cy+r),(56,cy+r)],'resultat',dash=True,lw=0.9)
text(ax,58,cy+r-0.5,'1 : point le plus haut','resultat','s',ha='left')
line(ax,[(4,cy+1.2*r),(56,cy+1.2*r)],'limite',lw=1.3)
text(ax,58,cy+1.2*r+1,r'$6\div5=1{,}2$','limite','s',ha='left')
text(ax,cx,cy-6,'cercle de rayon 1','sujet','s')
text(ax,44,5,'aucun point du cercle à la hauteur 1,2','limite','s')
save(fig,'35-085')
