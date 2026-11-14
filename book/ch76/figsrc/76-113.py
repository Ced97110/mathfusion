import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
u=5
def P(c,pts): return [(c[0]+x*u,c[1]+y*u) for x,y in pts]
y0=28
c1,c2,c3=(12,y0),(36,y0),(70,y0)
poly(ax,P(c1,[(-.5,-.5),(.5,-.5),(.5,.5),(-.5,.5)]),'sujet')
poly(ax,P(c2,[(0,-1),(1,0),(0,1),(-1,0)]),'varie')
poly(ax,P(c3,[(0,-1),(3,0),(0,1),(-3,0)]),'resultat')
arrow(ax,(17,y0),(29,y0),'fixe'); arrow(ax,(42,y0),(52,y0),'fixe')
text(ax,23,y0+4,r'$B$','fixe','l'); text(ax,47,y0+4,r'$A$','fixe','l')
text(ax,23,y0-4,r'$\times 2$','varie'); text(ax,47,y0-4,r'$\times 3$','varie')
for c,s,r in [(c1,'aire 1','sujet'),(c2,'aire 2','varie'),(c3,'aire 6','resultat')]:
    text(ax,c[0],14,s,r,'l')
text(ax,44,45,r'$\det(AB)=2\times3=6$','resultat','l')
save(fig,'76-113')
