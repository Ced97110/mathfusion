import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def cg(r,m): return rf'$x\equiv {r}\ (\mathrm{{mod}}\ {m})$'
for cx,r,m in [(16,2,3),(44,0,4),(72,1,5)]:
    box(ax,cx-12,66,24,9,'sujet',label=cg(r,m),size='s')
box(ax,16,44,28,9,'varie',label=cg(8,12),size='s')
box(ax,38,22,36,9,'resultat',label=cg(56,60),size='s')
arrow(ax,(16,66),(26,53),'varie'); arrow(ax,(44,66),(34,53),'varie')
arrow(ax,(30,44),(48,31),'varie'); arrow(ax,(72,66),(66,31),'varie')
text(ax,3,59,'fusion 1','varie','s',ha='left'); text(ax,3,37,'fusion 2','varie','s',ha='left')
text(ax,44,10,'12 et 5 : premiers entre eux','fixe','s')
save(fig,'52-197')
