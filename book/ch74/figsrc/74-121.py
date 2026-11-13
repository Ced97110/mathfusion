import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
rows = [('A : trace 0', 'trace 0', r'$P^{-1}AP$', 'resultat', 50), ('A = I : trace 2', 'trace 2', r'$P^{-1}AP$', 'resultat', 30), ('A = I : trace 2', 'trace 8', r'$PAP$', 'limite', 10)]
for l, r, a, role, y in rows:
    box(ax, 3, y, 27, 10, 'sujet', label=l, size='s')
    box(ax, 59, y, 26, 10, role, label=r, size='s')
    arrow(ax, (31, y + 5), (58, y + 5), role, lw=1.2)
    text(ax, 44.5, y + 8.6, a, role, 's')
save(fig, '74-121')
