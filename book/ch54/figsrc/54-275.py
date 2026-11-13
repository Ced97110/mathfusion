import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 84, r'Polynôme $x^2+1$, corps de départ ℝ', 'fixe', 's')
rows = [(64, 'fixe', 'ℝ', 'aucune racine', 'limite'),
        (40, 'autre', 'corps de rupture', r'une racine : $[x]$', 'varie'),
        (16, 'sujet', 'corps de décomposition', r'$(x-[x])(x+[x])$', 'resultat')]
for y, role, name, state, srole in rows:
    box(ax, 4, y, 38, 12, role, label=name, size='s')
    box(ax, 50, y, 34, 12, srole, label=state, size='s')
    arrow(ax, (42, y + 6), (50, y + 6), srole)
for y0, lab in [(64, 'ajouter une racine'), (40, 'répéter : tout se casse')]:
    arrow(ax, (23, y0 - 0.5), (23, y0 - 11.5), 'varie')
    text(ax, 44, y0 - 6, lab, 'varie', 's', ha='left') if False else None
    text(ax, 27, y0 - 6, lab, 'varie', 's', ha='left')
save(fig, '54-275')
