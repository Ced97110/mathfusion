import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'couples de $\mathbb{Z}\times2\mathbb{Z}$', 'sujet', 'm')
rows = [(48, ('(0, 2)', 'fixe'), ('(0, 4)', 'fixe'), ('(0, 8)', 'fixe'), 'comme 2 × 4 = 8'),
        (28, ('(1, 0)', 'sujet'), ('(0, 2)', 'fixe'), ('(0, 2)', 'fixe'), '(1, 0) agit comme 1'),
        (8, ('(1, −2)', 'autre'), ('(1, −2)', 'autre'), ('(1, 0)', 'resultat'), 'son propre inverse')]
for y, p, q, r, cap in rows:
    box(ax, 3, y, 22, 10, p[1], label=p[0], size='s')
    text(ax, 29, y + 5, r'$\times$', 'encre', 'm')
    box(ax, 33, y, 22, 10, q[1], label=q[0], size='s')
    text(ax, 59, y + 5, r'$=$', 'encre', 'm')
    box(ax, 63, y, 22, 10, r[1], label=r[0], size='s')
    text(ax, 44, y + 14, cap, r[1] if r[1] != 'fixe' else 'fixe', 's')
save(fig, '56-194')
