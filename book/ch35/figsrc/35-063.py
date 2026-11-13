import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
rows = [(64, 'produit → somme', 'fixe', '2 sin 45° cos 15°', 'sin 60° + sin 30°'),
        (40, 'somme → produit : factorisation', 'sujet', 'sin 75° + sin 15°', '2 sin 45° cos 30°'),
        (16, 'chapitre 18 : nombres ordinaires', 'autre', '15 + 5', '5 × (3 + 1)')]
for y, tag, role, a, b in rows:
    text(ax, 2, y + 3, tag, role, 's', ha='left', weight='bold' if role == 'sujet' else 'normal')
    box(ax, 2, y - 12, 36, 11, role, label=a, size='s')
    box(ax, 50, y - 12, 36, 11, role, label=b, size='s')
    arrow(ax, (38.5, y - 6.5), (49.5, y - 6.5), 'varie', lw=1.2)
save(fig, '35-063')
