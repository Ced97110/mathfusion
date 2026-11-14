import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def seg(ax,p,q,r,role='fixe',lw=0.8,dash=False):
    n=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/n,(q[1]-p[1])/n
    line(ax,[(p[0]+ux*r,p[1]+uy*r),(q[0]-ux*r,q[1]-uy*r)],role,lw,dash)

fig,ax=canvas(84)
line(ax,[(50,4),(50,82)],'fixe',0.8,True)
text(ax,26,80,'chaîne','sujet','l'); text(ax,68,80,'sans « chaîne »','limite','l')
r=4
seg(ax,(9,26),(9,58),r,'fixe',1.4)
disc(ax,9,26,r,'sujet',label='a'); disc(ax,9,58,r,'autre',label='b')
text(ax,16,58,'a ∨ b = b : le plus grand','resultat','s',ha='left')
text(ax,16,26,'a ∧ b = a : le plus petit','resultat','s',ha='left')
text(ax,16,42,'a ≤ b','encre','m',ha='left')
# counter-example : 2 and 3 below, their common upper bounds 12 and 18 in a box
box(ax,53,40,32,26,'varie',fill=False,dash=True)
text(ax,69,71,'majorants de 2 et 3','varie','s')
t12=(62,57); t18=(77,57); b2=(61,20); b3=(77,20)
disc(ax,*t12,r,'varie',label='12'); disc(ax,*t18,r,'varie',label='18')
line(ax,[(t12[0]+r+1,57),(t18[0]-r-1,57)],'limite',1.0,True)
text(ax,69,44,'12 et 18 incomparables','limite','s')
disc(ax,*b2,r,'sujet',label='2'); disc(ax,*b3,r,'sujet',label='3')
for b in (b2,b3):
    n=math.hypot(69-b[0],40-b[1]); line(ax,[(b[0]+(69-b[0])/n*r,b[1]+(40-b[1])/n*r),(69,40)],'fixe',0.9)
text(ax,69,8,"2 ∨ 3 n'existe pas",'limite','s')
save(fig,'79-048')
