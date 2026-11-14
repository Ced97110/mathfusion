import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(98)
box(ax,14,4,60,70,'resultat',fill=False,dash=True)
text(ax,44,79,'sous x, x compris','resultat','s')
text(ax,44,90,r'$g$(6) = 1 + 2 + 3 + 6 = 12','resultat','m')
pos={1:(44,14),2:(26,38),3:(62,38),6:(44,62)}
for a,b in ((1,2),(1,3),(2,6),(3,6)): line(ax,[pos[a],pos[b]],'fixe')
for n,(x,y) in pos.items(): disc(ax,x,y,5,'sujet' if n==6 else 'resultat',label=str(n))
text(ax,53,62,r'$x$ = 6','sujet','s',ha='left')
[l.set_zorder(1.5) for l in ax.lines]
save(fig,'80-249')
