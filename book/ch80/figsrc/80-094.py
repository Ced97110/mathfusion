import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def horiz(ax, o, u, a, role, fill=True, lw=0.8):
    poly(ax, [iso(a, a, 0, o, u), iso(-a, a, 0, o, u), iso(-a, -a, 0, o, u), iso(a, -a, 0, o, u)], role, fill=fill, lw=lw)
def vert(ax, o, u, a, b, role, fill=True, lw=0.8):
    poly(ax, [iso(0, a, b, o, u), iso(0, -a, b, o, u), iso(0, -a, -b, o, u), iso(0, a, -b, o, u)], role, fill=fill, lw=lw)

fig,ax=canvas(70)
o=(30,36); u=10
horiz(ax,o,u,1.2,'sujet',lw=1.0)
vert(ax,o,u,1.2,1.0,'varie',fill=False,lw=1.2)
line(ax,[iso(0,-1.2,0,o,u),iso(0,1.2,0,o,u)],'resultat',lw=2.4)
text(ax,70,60,'plan horizontal','sujet','s')
text(ax,70,50,'plan vertical','varie','s')
text(ax,66,38,'intersection : axe de la largeur','resultat','s')
text(ax,66,31,'dimension 1','resultat','s')
text(ax,44,10,'somme : l’espace entier, dim 3','encre','m')
save(fig,'80-094')
