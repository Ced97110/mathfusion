import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pol(c,r,a): return (c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a)))
def arc(ax,c,r,a0,a1,role,lw=0.9,head=False):
    pts=[pol(c,r,a0+(a1-a0)*i/40) for i in range(41)]
    line(ax,pts,role,lw)
    if head: arrow(ax,pts[-3],pts[-1],role,lw)

fig,ax=canvas(60)
x0=14; U=60
text(ax,44,54,'somme des tangentes','encre','m')
box(ax,x0,40,U/2,7,'sujet',label='1/2'); box(ax,x0+U/2,40,U/3,7,'autre',label='1/3')
text(ax,44,32,'1 − produit des tangentes','encre','m')
box(ax,x0,22,U*5/6,7,'fixe',label='1 − 1/6'); box(ax,x0+U*5/6,22,U/6,7,'varie',label='1/6',dash=True)
line(ax,[(x0+U*5/6,18),(x0+U*5/6,49)],'resultat',1.1,dash=True)
text(ax,x0+U*5/6,14,'5/6','resultat','m')
text(ax,44,5,'5/6 ÷ 5/6 = 1','resultat','l')
save(fig,'33-145')
