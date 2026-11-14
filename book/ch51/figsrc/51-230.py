import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def link(p,q,r1,r2,role="fixe",lw=1.0):
    dx,dy=q[0]-p[0],q[1]-p[1]; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(p[0]+ux*r1,p[1]+uy*r1),(q[0]-ux*r2,q[1]-uy*r2),role,lw)
text(ax,4,84,'cadran à 7 : ×3','fixe','m',ha='left')
for (v,w,y) in ((2,6,74),(3,2,62)):
    disc(ax,12,y,3.5,'sujet',label=str(v)); disc(ax,50,y,3.5,'resultat',label=str(w)); link((12,y),(50,y),3.5,3.5,'resultat',1.2)
text(ax,72,68,r'$6\neq2$','resultat','l')
text(ax,4,46,'cadran à 6 : ×2','fixe','m',ha='left')
disc(ax,12,36,3.5,'sujet',label='1'); disc(ax,12,24,3.5,'sujet',label='4'); disc(ax,50,30,3.5,'limite',label='2')
link((12,36),(50,30),3.5,3.5,'limite',1.2); link((12,24),(50,30),3.5,3.5,'limite',1.2)
text(ax,70,30,'même arrivée','limite','s')
text(ax,44,8,r'$ax_1=ax_2\Rightarrow x_1=x_2$','sujet','m')
save(fig,'51-230')
