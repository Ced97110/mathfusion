import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
f=numberline(ax,10,70,14,0,2.5,step=0.5)
for v,l,r,h in ((1,'100 % = 1','fixe',22),(1.65,'165 % = 1,65','sujet',29),(2.1,'210 % = 2,1','autre',37)):
    line(ax,[(f(v),15.5),(f(v),h-1.5)],r,dash=True); disc(ax,f(v),14,1.2,r); text(ax,f(v),h,l,r,'s')
text(ax,44,3.5,'pourcentage ÷ 100 = décimal','encre','s')
save(fig,'09-111')
