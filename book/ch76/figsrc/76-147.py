import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64); s=9
def draw(O,cols,role,l1,l2,tag):
    P=lambda a,b:(O[0]+a*s,O[1]+b*s)
    (a,b),(c,d)=cols
    poly(ax,[P(0,0),P(a,b),P(a+c,b+d),P(c,d)],role)
    poly(ax,[P(0,0),P(1,0),P(1,1),P(0,1)],'fixe',fill=False)
    arrow(ax,P(0,0),P(a,b),role,lw=1.1); arrow(ax,P(0,0),P(c,d),role,lw=1.1)
draw((8,8),((1,0),(1,1)),'resultat','','','')
draw((52,8),((2,1),(1,3)),'limite','','','')
line(ax,[(44,6),(44,62)],'fixe',lw=0.6,dash=True)
text(ax,24,59,r'$\det=1$','resultat','l'); text(ax,24,52,'aire 1 → aire 1','resultat','s')
text(ax,66,59,r'$\det=5$','limite','l'); text(ax,66,52,'aire 1 → aire 5','limite','s')
text(ax,24,3.2,'dans $SL_2$','resultat','s'); text(ax,66,3.2,'hors de $SL_2$','limite','s')
save(fig,'76-147')
