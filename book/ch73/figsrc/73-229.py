import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
o=(8,10); u=5.0
P=lambda x,y:(o[0]+x*u,o[1]+y*u)
arrow(ax,P(0,0),P(3,4),'sujet',lw=1.4); arrow(ax,P(0,0),P(5,0),'autre',lw=1.4)
line(ax,[P(3,4),P(8,4)],'fixe',lw=0.6,dash=True); line(ax,[P(5,0),P(8,4)],'fixe',lw=0.6,dash=True)
arrow(ax,P(0,0),P(8,4),'resultat',lw=1.4)
text(ax,P(1.5,2)[0]-8,P(1.5,2)[1]+2,r'$x$ : 5','sujet','s')
text(ax,P(2.5,0)[0],P(2.5,0)[1]-3.5,r'$y$ : 5','autre','s')
text(ax,50,36,r'$\Vert x+y\Vert^2=80$','resultat','s',ha='left')
box(ax,50,6,34,14,'resultat',label=r'$\frac{1}{2}(80-25-25)=15$',size='m')
text(ax,67,26,r'$\langle x,y\rangle=15$','resultat','s')
save(fig,'73-229')
