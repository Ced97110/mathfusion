import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
steps = [
    ('sujet', r'$f$ (degré 4) : $G_f$ inconnu'),
    ('autre', r'$g$ (degré 3) : polynôme auxiliaire'),
    ('autre', r'ordre du groupe de $g$'),
    ('resultat', r'$G_f$ lu à partir de cet ordre'),
]
acts = ['construire', 'calculer (degré 3)', 'lire']
y = 66
for i, (role, lab) in enumerate(steps):
    box(ax, 6, y, 76, 10, role, label=lab, size='s')
    if i < 3:
        arrow(ax, (30, y), (30, y - 6), 'varie')
        text(ax, 36, y - 3, acts[i], 'varie', 's', ha='left')
    y -= 17
save(fig, '65-095')
