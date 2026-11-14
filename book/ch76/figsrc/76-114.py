import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
u=6
def P(c,pts): return [(c[0]+x*u,c[1]+y*u) for x,y in pts]
sq=[(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)]
y1=70
poly(ax,P((10,y1),sq),'sujet'); poly(ax,P((40,y1),[(-1.5,-.5),(1.5,-.5),(1.5,.5),(-1.5,.5)]),'varie'); poly(ax,P((76,y1),sq),'sujet')
arrow(ax,(15,y1),(31,y1),'varie'); arrow(ax,(49,y1),(71,y1),'varie')
text(ax,23,y1+4,r'$\times 3$','varie'); text(ax,60,y1+4,r'$\times\frac{1}{3}$','varie')
for x,s in [(10,'aire 1'),(40,'aire 3'),(76,'aire 1')]: text(ax,x,y1-8,s,'sujet')
text(ax,44,50,r'$3\times\frac{1}{3}=1$','resultat','l')
y2=22
poly(ax,P((10,y2),sq),'sujet'); line(ax,[(34,y2-4),(46,y2+4)],'limite',lw=1.6)
arrow(ax,(15,y2),(31,y2),'varie'); text(ax,23,y2+4,r'$\det=0$','limite')
line(ax,[(50,y2),(70,y2)],'limite',dash=True); text(ax,60,y2,r'$\times$','limite','l')
text(ax,40,y2-9,'aire 0','limite'); text(ax,60,y2-9,'aucun retour','limite')
save(fig,'76-114')
