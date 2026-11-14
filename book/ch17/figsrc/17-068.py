import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,12,62,18,9,'sujet',label=r'$1$'); text(ax,44,66.5,r'$<$','varie','l'); box(ax,58,62,18,9,'autre',label=r'$3$')
arrow(ax,(44,60),(44,48),'varie'); text(ax,60,54,r'$\times(-1)$','varie','s',ha='left')
box(ax,12,36,18,9,'sujet',label=r'$-1$'); text(ax,44,40.5,r'$>$','varie','l'); box(ax,58,36,18,9,'autre',label=r'$-3$')
text(ax,44,29,'symbole retourné','varie','s')
f=numberline(ax,14,74,14,-4,4,labels=False,arrow_right=False)
for v,r,l in ((1,'sujet','1'),(3,'autre','3'),(-1,'sujet','-1'),(-3,'autre','-3')): disc(ax,f(v),14,3.2,r,label=f'${l}$',size='s')
for pt in ax.patches:
    if pt.__class__.__name__=='Circle': pt.set_zorder(3.5)
save(fig,'17-068')
