import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# preuve : départ, développement en deux lignes reconnues comme cos(30°+45°) et sin(30°+45°), arrivée
fig, ax = canvas(92)
box(ax, 2, 78, 84, 10, 'sujet', label='zw = 2 cis 30° × √2 cis 45°', size='s')
box(ax, 2, 62, 84, 10, 'fixe', label='= 2√2 × (cis 30° × cis 45°)', size='s')
box(ax, 2, 24, 84, 32, 'varie', lw=1.8)
text(ax, 44, 51.5, 'cis 30° × cis 45° développé :', 'varie', 's')
rows = ((41, 'partie réelle', r'$\cos30°\cos45°-\sin30°\sin45°$', r'$\cos(30°+45°)$'),
        (30, 'partie imaginaire', r'$\sin30°\cos45°+\cos30°\sin45°$', r'$\sin(30°+45°)$'))
for y, lab, expr, res in rows:
    text(ax, 4, y + 3.8, lab, 'varie', 's', ha='left')
    text(ax, 4, y - 1, expr, 'varie', 's', ha='left')
    arrow(ax, (47, y - 1), (53, y - 1), 'varie', lw=1.0)
    text(ax, 55, y - 1, res, 'resultat', 's', ha='left')
box(ax, 2, 6, 84, 11, 'resultat', label='zw = 2√2 cis 75°', size='m', weight='bold')
for y0, y1 in ((78, 73.3), (62, 57.3), (24, 18.3)):
    arrow(ax, (44, y0), (44, y1), 'fixe', lw=0.9)
save(fig, '39-067')
