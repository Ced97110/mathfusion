import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def horiz(ax, o, u, a, role, fill=True, lw=0.8):
    poly(ax, [iso(a, a, 0, o, u), iso(-a, a, 0, o, u), iso(-a, -a, 0, o, u), iso(a, -a, 0, o, u)], role, fill=fill, lw=lw)
def vert(ax, o, u, a, b, role, fill=True, lw=0.8):
    poly(ax, [iso(0, a, b, o, u), iso(0, -a, b, o, u), iso(0, -a, -b, o, u), iso(0, a, -b, o, u)], role, fill=fill, lw=lw)

fig,ax=canvas(66)
o=(22,34); u=9
vert(ax,o,u,1.2,1.0,'varie',fill=False,lw=1.0)
horiz(ax,o,u,1.2,'sujet',lw=1.0)
vert(ax,o,u,1.2,1.0,'varie',fill=False,lw=1.0)
line(ax,[iso(0,-1.2,0,o,u),iso(0,1.2,0,o,u)],'resultat',lw=2.4)
text(ax,22,60,'deux plans distincts','encre','s')
text(ax,22,8,'droite commune = un point','resultat','s')
o2=(66,34)
horiz(ax,o2,u,1.2,'sujet',lw=1.0)
poly(ax,[iso(1.2,1.2,0,o2,u),iso(-1.2,1.2,0,o2,u),iso(-1.2,-1.2,0,o2,u),iso(1.2,-1.2,0,o2,u)],'varie',fill=False,lw=1.0)
text(ax,66,60,'le même plan deux fois','encre','s')
text(ax,66,8,'tout le plan : pas un point','limite','s')
save(fig,'80-093')
