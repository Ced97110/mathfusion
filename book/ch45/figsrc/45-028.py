import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for i, (sym, role, t) in enumerate(((r'$\neq$', 'limite', 'éléments : pas égaux'), (r'$\cong$', 'resultat', 'structure : la même'))):
    y = 40 - 28 * i + 6
    box(ax, 3, y - 6, 28, 12, 'sujet', label=r'$G$ : 0 1 2 3', size='s')
    box(ax, 57, y - 6, 28, 12, 'autre', label=r"$G'$ : $r_0$ $r_1$ $r_2$ $r_3$", size='s')
    text(ax, 44, y, sym, role, 'xl')
    text(ax, 44, y - 9, t, role, 's')
text(ax, 44, 59, r'$G\cong G^{\prime}$ : isomorphe à', 'encre', 'm')
save(fig, '45-028')
