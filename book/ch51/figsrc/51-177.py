import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
P={'i':(9,13),'j':(39,13),'k':(24,40)}
R=4.4
def edge(a,b,role,curve=0.0):
    (x0,y0),(x1,y1)=P[a],P[b]; dx,dy=x1-x0,y1-y0; d=math.hypot(dx,dy); ux,uy=dx/d,dy/d
    arrow(ax,(x0+ux*R,y0+uy*R),(x1-ux*R,y1-uy*R),role,lw=1.1,curve=curve)
for a,b in [('i','j'),('j','k'),('k','i')]:
    edge(a,b,'sujet'); edge(b,a,'varie',-0.35)
for n,(x,y) in P.items(): disc(ax,x,y,R,'fixe',label='$'+n+'$',size='l')
text(ax,70,57,'avec la flèche : +','sujet','s')
for y,s in zip([50,43,36],['ij=k','jk=i','ki=j']): text(ax,70,y,'$'+s+'$','sujet','m')
text(ax,70,27,'contre la flèche : −','varie','s')
for y,s in zip([20,13,6],['ji=-k','kj=-i','ik=-j']): text(ax,70,y,'$'+s+'$','varie','m')
save(fig,'51-177')
