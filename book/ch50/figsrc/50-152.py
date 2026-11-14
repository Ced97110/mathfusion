import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
items = [(58, 'sujet', 'on suppose $H$\nde 6 éléments', 'départ'),
         (33, 'varie', 'indice 2 : le carré de\ntout élément est dans $H$', 'étape clé'),
         (8, 'limite', 'contradiction\navec $|H| = 6$', 'arrivée')]
for y, r, s, tag in items:
    box(ax, 22, y, 60, 14, r, label=s, size='s', lw=1.6 if r == 'varie' else 0.8)
    text(ax, 2, y + 7, tag, r, 's', ha='left')
arrow(ax, (52, 57.2), (52, 48.8), 'fixe'); arrow(ax, (52, 32.2), (52, 23.8), 'fixe')
save(fig, '50-152')
