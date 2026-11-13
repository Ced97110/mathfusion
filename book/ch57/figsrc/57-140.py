import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
rows = [  # (label, boxes, result)
    ('un multiple', [r'$3\times(2\,;\,1)$'], r'$=(6\,;\,3)$'),
    ('une somme', [r'$1\times(2\,;\,1)$', r'$1\times(1\,;\,1)$'], r'$=(3\,;\,2)$'),
    ('combinaison', [r'$3\times(2\,;\,1)$', r'$-2\times(1\,;\,1)$'], r'$=(4\,;\,1)$'),
]
for k, (lab, bx, res) in enumerate(rows):
    y = 54 - k * 19
    text(ax, 2, y + 5, lab, 'encre', 's', ha='left')
    x = 24
    for n, b in enumerate(bx):
        if n: text(ax, x - 2.5, y + 5, '+', 'encre', 'm');
        box(ax, x, y, 20, 10, 'sujet' if k < 2 else 'varie', label=b, size='s')
        x += 25
    text(ax, 69 if len(bx) == 2 else 47, y + 5, res, 'resultat', 's', ha='left')
text(ax, 44, 6, 'des éléments × des coefficients, puis +', 'encre', 's')
save(fig, '57-140')
