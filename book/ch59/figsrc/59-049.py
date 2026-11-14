import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def mat(x, rows, role):
    for i, vals in enumerate(rows):
        for j, v in enumerate(vals):
            box(ax, x + j * 11, 39 - i * 10, 11, 10, role, label=v)
text(ax, 44, 69, r'inversible sur $\mathbb{Z}$ $\Leftrightarrow$ $\det=\pm1$', 'encre', 'm')
mat(7, [('2', '1'), ('1', '1')], 'sujet')
mat(58, [('1', '−1'), ('−1', '2')], 'resultat')
text(ax, 18, 56, r'$A$', 'sujet', 'l'); text(ax, 69, 56, 'inverse de $A$', 'resultat', 'm')
arrow(ax, (31, 39), (56, 39), 'varie', lw=1.2)
text(ax, 18, 25, r'$\det=2\cdot1-1\cdot1=1$', 'resultat', 's')
text(ax, 69, 25, 'tous entiers : oui', 'resultat', 's')
line(ax, [(4, 19), (84, 19)], 'fixe', lw=0.6, dash=True)
box(ax, 8, 2, 72, 13, 'limite', label=r'$\det\neq\pm1$ : l’inverse divise par $\det$' + '\net sort des entiers : non inversible', size='s')
save(fig, '59-049')
