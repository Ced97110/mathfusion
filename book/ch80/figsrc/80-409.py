import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
cols = [(12, 'sujet', 'Entiers\nsommes', [r"$x+y$", r"$-x$", r"$x+y=y+x$"]),
        (56, 'autre', 'Rationnels non nuls\nproduits', [r"$x\times y$", r"$1/x$", r"$x\times y=y\times x$"])]
labels = ['combiner', 'revenir en arrière', "changer l'ordre"]
for x, role, head, cells in cols:
    box(ax, x, 51, 30, 11, role, label=head, size='s')
    for i, c in enumerate(cells):
        box(ax, x, 38 - 14 * i, 30, 10, role, label=c, size='s')
for i, l in enumerate(labels):
    text(ax, 6, 43 - 14 * i, l.replace(' ', '\n', 1) if len(l) > 10 else l, 'fixe', 's')
text(ax, 44, 4, 'mêmes trois gestes, même résultat', 'resultat', 's')
save(fig, '80-409')
