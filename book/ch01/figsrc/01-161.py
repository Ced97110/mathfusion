import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(100)
text(ax,4,90,'départ','resultat','m',ha='left')
disc(ax,24,90,3,'resultat'); text(ax,24,90,'2','encre','m')
text(ax,56,90,"produit d'un seul insécable",'resultat','s')
text(ax,44,79,"s'il est insécable : fini",'fixe','s')
X=lambda c: 10+5.5*(c-2)
for c in range(2,13): box(ax,X(c),52,5.5,6,'varie' if c==12 else 'sujet',r=0.5)
for c in (3,4): box(ax,X(c),52,5.5,6,'varie',fill=False,r=0.5,lw=1.8)
brace(ax,10,65,50,'sujet','supposés vrais : 2 à 11')
arrow(ax,(67.75,58),(18.25,58),'varie',curve=0.25); arrow(ax,(67.75,58),(23.75,58),'varie',curve=0.2)
text(ax,44,70,'12 = 3 × 4','varie','m')
box(ax,6,40,76,34,'varie',fill=False,dash=True)
text(ax,80,76.5,'étape clé','varie','s',ha='right')
def edge(p,q,r=3):
    d=math.hypot(q[0]-p[0],q[1]-p[1]); u=((q[0]-p[0])/d,(q[1]-p[1])/d)
    line(ax,[(p[0]+u[0]*r,p[1]+u[1]*r),(q[0]-u[0]*r,q[1]-u[1]*r)],'fixe')
for p,q in (((44,32),(30,22)),((44,32),(58,22)),((58,22),(50,11)),((58,22),(66,11))): edge(p,q)
for (x,y),r,l in (((44,32),'varie','12'),((30,22),'resultat','3'),((58,22),'fixe','4'),((50,11),'resultat','2'),((66,11),'resultat','2')):
    disc(ax,x,y,3,r); text(ax,x,y,l,'encre','m')
text(ax,16,8,'12 = 3 × 2 × 2','resultat','m')
save(fig,'01-161')
