import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = ((46, r'$x+3=7$', '4', 'un nombre'), (22, r'$x+3=b$', r'$b-3$', r'écrit avec $b$'))
for y, eq, r, tag in rows:
    box(ax, 2, y, 28, 10, 'fixe', label=eq)
    arrow(ax, (31, y + 5), (45, y + 5), 'varie'); text(ax, 38, y + 9, 'isoler', 'varie', 's')
    box(ax, 46, y, 12, 10, 'sujet', label=r'$x$'); text(ax, 62, y + 5, '=', 'encre', 'm')
    box(ax, 66, y, 20, 10, 'resultat', label=r if r.startswith('$') else r)
    text(ax, 76, y - 4, tag, 'resultat', 's')
text(ax, 44, 6, r'$x$ est seul d’un côté dans les deux cas', 'sujet', 's')
text(ax, 52, 60, r'$x$ seul', 'sujet', 's')
save(fig, '16-059')
