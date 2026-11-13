import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,53,'18 = 252 × 4 + 198 × (−5)','encre','l')
s=80/1008; x0=4
text(ax,x0,44.5,r'$u = 4$ : coefficient de 252','sujet','s',ha='left')
box(ax,x0,34,80,8,'sujet',label='252 × 4 = 1 008')
text(ax,x0,29,r'$v = -5$ : coefficient de 198','autre','s',ha='left')
w2=990*s
box(ax,x0,18,w2,8,'autre',label='198 × 5 = 990')
ax.add_patch(Rectangle((x0+w2,18),80-w2,8,fc=FILL['resultat'],ec=COL['resultat'],lw=0.8,zorder=2))
line(ax,[(x0+80,43),(x0+80,17)],'fixe',dash=True)
text(ax,56,8,'1 008 − 990 = 18','resultat','m')
arrow(ax,(70,9.5),(x0+w2+(80-w2)/2,17),'resultat')
save(fig,'05-145')
