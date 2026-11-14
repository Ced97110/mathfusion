import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (16, 12); u = 10
for v, role, lab, dx, dy in [((1, 0, 0), 'sujet', r'$i$', 2.5, 0), ((0, 1, 0), 'varie', r'$j$', -2.5, 0), ((0, 0, 1), 'fixe', r'$k$', 0, 2.5)]:
    p = iso(*v, origin=o, u=u); arrow(ax, o, p, role); text(ax, p[0] + dx, p[1] + dy, lab, role, 'm')
text(ax, 16, 4, r'$\mathbb{R}^3$', 'sujet', 'm')
box(ax, 30, 44, 56, 11, 'fixe', label=r'$(i\times i)\times j=0$')
box(ax, 30, 29, 56, 11, 'varie', label=r'$(i\times j)\times i=k\times i=j$')
box(ax, 30, 14, 56, 11, 'varie', label=r'$(j\times i)\times i=-j$')
box(ax, 30, 0.5, 56, 11, 'resultat', label=r'$0+j-j=0$', weight='bold')
for y in (44, 29, 14): arrow(ax, (58, y), (58, y - 4), 'fixe')
save(fig, '78-059')
