import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 13, 66, '$M$ (départ)', 'sujet', 'm')
text(ax, 69, 66, '$N$ (arrivée)', 'autre', 'm')
rows = [(52, '(1, 0)', '(2, 1)', 'varie', 'imposé'),
        (36, '(0, 1)', '(1, 3)', 'varie', 'imposé'),
        (16, '(5, 4)', '5 (2, 1) + 4 (1, 3)', 'resultat', 'forcé')]
for cy, a, b, role, tag in rows:
    box(ax, 2, cy - 5, 22, 10, 'sujet', label=a)
    box(ax, 50, cy - 5, 36, 10, 'autre', label=b)
    arrow(ax, (24, cy), (50, cy), role)
    text(ax, 37, cy + 3.2, tag, role, 's')
text(ax, 13, 26, '⋮', 'fixe', 'l')
text(ax, 44, 4, 'aucun autre choix possible', 'resultat', 's')
save(fig, '58-063')
