import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
y=20
f=numberline(ax,8,70,y,-6,6,every=3)
box(ax,f(-6),25,f(0)-f(-6)-0.5,11,'sujet',label=r'$a<0$',size='l')
box(ax,f(0)+0.5,25,f(6)-f(0)-0.5,11,'fixe',label=r'$a\geq0$',size='l')
for v,role,lab in [(-5,'resultat',r'$a=-5$ : vrai'),(0,'limite',r'$a=0$ : faux'),(5,'limite',r'$a=5$ : faux')]:
    disc(ax,f(v),y,1.4,role)
    text(ax,f(v)+(2 if v==-5 else 0),10.5,lab,role,'s')
save(fig,'13-049')
