import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,54,r'$x^2=7$','sujet','xl')
f=numberline(ax,10,78,30,-4,4,every=4,arrow_right=False)
r=7**0.5
disc(ax,f(-r),30,1.8,'resultat'); disc(ax,f(r),30,1.8,'resultat')
text(ax,f(-r),37,r'$-\sqrt{7}\approx-2{,}646$','resultat','s',ha='right')
text(ax,f(r),37,r'$\sqrt{7}\approx2{,}646$','resultat','s',ha='left')
arrow(ax,(f(-r)+2,44),(f(r)-2,44),'varie',both=True); text(ax,44,48,'opposés','varie','s')
box(ax,10,4,68,10,'resultat',label='deux solutions : √7 et −√7')
save(fig,'22-147')
