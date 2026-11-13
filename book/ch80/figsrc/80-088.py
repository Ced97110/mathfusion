import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(68)
o=(36,26); u=12
poly(ax,[iso(-1.2,-1.2,1,o,u),iso(1.8,-1.2,1,o,u),iso(1.8,1.8,1,o,u),iso(-1.2,1.8,1,o,u)],'fixe',lw=0.8)
a=iso(-1.5,1.5,0,o,u); b=iso(1.5,-1.5,0,o,u)
line(ax,[a,b],'limite',lw=1.8)
line(ax,[o,iso(1,1,2,o,u)],'sujet',lw=1.8)
line(ax,[o,iso(0,0,1,o,u)],'fixe',lw=0.9,dash=True)
c=iso(0.5,0.5,1,o,u)
disc(ax,c[0],c[1],1.8,'resultat')
disc(ax,o[0],o[1],1.2,'encre')
text(ax,3,63,'feuille : hauteur 1','fixe','s',ha='left')
text(ax,39,49,'monte : 1 point','resultat','s',ha='left')
text(ax,52,21.5,'horizontale : aucun point','limite','s')
text(ax,24,21.5,'origine','encre','s')
save(fig,'80-088')
