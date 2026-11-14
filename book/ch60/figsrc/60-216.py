import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
c1, c2 = 22, 66
text(ax, c1, 82, 'chaîne 1', 'sujet', 'm', weight='bold')
text(ax, c2, 82, 'chaîne 2', 'autre', 'm', weight='bold')
box(ax, c1 - 19, 62, 38, 10, 'sujet', label=r'$v=(1,0,0)$')
box(ax, c1 - 19, 36, 38, 10, 'sujet', label=r'$w=(-2,-1,-1)$')
box(ax, c1 - 19, 10, 38, 10, 'resultat', label=r'$0$ (vecteur nul)', size='s')
box(ax, c2 - 19, 62, 38, 10, 'autre', label=r'$u=(1,-1,0)$')
box(ax, c2 - 19, 36, 38, 10, 'resultat', label=r'$0$ (vecteur nul)', size='s')
for x, ys, role in ((c1, (61, 47, 35, 21), 'sujet'), (c2, (61, 47), 'autre')):
    arrow(ax, (x, 61), (x, 47.5), role)
    text(ax, x + 2, 54, r'$A-1$', role, 'm', ha='left')
arrow(ax, (c1, 35), (c1, 21.5), 'sujet')
text(ax, c1 + 2, 28, r'$A-1$', 'sujet', 'm', ha='left')
save(fig, '60-216')
