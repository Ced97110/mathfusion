import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def mat(x, rows, role):
    for i, vals in enumerate(rows):
        for j, v in enumerate(vals):
            box(ax, x + j * 11, 51 - i * 10, 11, 10, role, label=v)
mat(7, [('2', '1'), ('1', '1')], 'sujet')
mat(58, [('1', '0'), ('0', '1')], 'resultat')
text(ax, 18, 74, r'$A$ inversible', 'sujet', 'm'); text(ax, 69, 74, 'identité', 'resultat', 'm')
arrow(ax, (31, 51), (56, 51), 'varie', lw=1.2)
text(ax, 43.5, 56, 'lignes et colonnes', 'varie', 's')
text(ax, 18, 37, r'$\det=2\times1-1\times1=1$', 'sujet', 's')
text(ax, 69, 37, r'$d_1=d_2=1$', 'resultat', 'm')
text(ax, 44, 28, r'$1\times y_i=0$ donne $y_i=0$', 'encre', 's')
arrow(ax, (44, 24.5), (44, 19), 'varie')
box(ax, 22, 5, 44, 13, 'resultat', label=r'$M=\{0\}$ : rien ne reste', size='m')
save(fig, '59-130')
