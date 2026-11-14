import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
y=62
box(ax,4,y-5,16,10,'sujet',label=r'$a\,x$'); text(ax,24,y,'+','encre','l'); box(ax,28,y-5,16,10,'sujet',label=r'$b\,y$')
text(ax,66,y,'linéaire','resultat','l',weight='bold')
y=38
box(ax,4,y-5,16,10,'sujet',label=r'$x$'); text(ax,24,y,'+','encre','l'); box(ax,28,y-5,16,10,'limite',label='1')
text(ax,66,y,'pas linéaire','limite','l',weight='bold'); text(ax,36,y-9,'1 : pas un multiple de x','limite','s')
y=14
box(ax,4,y-5,16,10,'limite',label=r'$x^2$')
text(ax,66,y,'pas linéaire','limite','l',weight='bold'); text(ax,24,y,r'pas « nombre fixe × $x$ »','limite','s',ha='left')
save(fig,'42-254')
