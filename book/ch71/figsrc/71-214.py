import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
o = (28, 32); u = 14
ax.add_patch(Circle(o, u, ec=COL['sujet'], fc='none', lw=1.0, zorder=2))
ax.add_patch(Circle(o, u*2**0.5, ec=COL['autre'], fc='none', lw=1.0, ls='--', zorder=2))
arrow(ax, (o[0]-23, o[1]), (o[0]+23, o[1]), 'fixe', lw=0.6); arrow(ax, (o[0], o[1]-23), (o[0], o[1]+24), 'fixe', lw=0.6)
disc(ax, o[0]+u, o[1], 1.2, 'sujet', fill=True); disc(ax, o[0]+u, o[1]+u, 1.2, 'autre', fill=True)
text(ax, o[0]+u+1.5, o[1]-4, r'$(1,\ 0)$', 'sujet', 's', ha='left')
text(ax, o[0]+u+2, o[1]+u+3.5, r'$(1,\ 1)$', 'autre', 's', ha='left')
arrow(ax, (o[0]+u+1.2, o[1]+1.5), (o[0]+u+1.2, o[1]+u-1.5), 'varie', curve=0.0)
text(ax, 72, 54, r'$Q(1,0)=1$', 'sujet', 's'); text(ax, 72, 48, r'$Q(1,1)=2$', 'autre', 's')
text(ax, 72, 36, 'sans B : possible', 'resultat', 's')
text(ax, 72, 24, 'en conservant B :', 'limite', 's'); text(ax, 72, 19, r'impossible, $1\neq2$', 'limite', 's')
save(fig, '71-214')
