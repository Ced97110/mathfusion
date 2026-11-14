import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
f=numberline(ax,6,76,38,-6,12,labels=False,arrow_right=False)
for v in (-6,0,6,12):
    disc(ax,f(v),38,1.8,'sujet'); text(ax,f(v),32,str(v),'sujet','s')
    arrow(ax,(f(v),35.5),(f(v),24),'resultat')
disc(ax,f(7),38,1.8,'varie'); text(ax,f(7)+1,32,'7','varie','s')
box(ax,56,56,28,10,'autre',label='(1, 1)',size='m')
arrow(ax,(f(7),40.5),(f(7)+2,56),'varie'); text(ax,f(7)+6.5,49,'η','varie','s')
box(ax,6,12,76,10,'resultat',label='(0, 0) : noyau 6ℤ',size='m')
text(ax,4,56,'η(n) = (n mod 2, n mod 3)','encre','s',ha='left')
save(fig,'52-173')
