import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 18, 56, r'$\Lambda(V)$', 'sujet', 'm'); text(ax, 68, 56, '$A$ : tableaux', 'autre', 'm')
box(ax, 4, 38, 28, 9, 'sujet', label=r'$e_1$')
box(ax, 2, 14, 32, 9, 'sujet', label=r'$e_1\wedge e_1=0$', size='s')
arrow(ax, (18, 38), (18, 23.5), 'varie'); text(ax, 24, 31, '× lui-même', 'varie', 's')
arrow(ax, (35, 42.5), (48, 42.5), 'varie'); text(ax, 41.5, 46, '$L$', 'varie', 's')
def mat(x0, y0, vals, role):
    for k, v in enumerate(vals):
        box(ax, x0 + (k % 2) * 9, y0 + (1 - k // 2) * 9, 9, 9, role, label=v)
mat(52, 33, ['0', '1', '0', '0'], 'autre')
arrow(ax, (61, 32), (61, 23.5), 'varie'); text(ax, 68, 28, 'au carré', 'varie', 's')
mat(52, 3, ['0', '0', '0', '0'], 'resultat')
arrow(ax, (36, 18.5), (50, 8), 'resultat', curve=0.0)
save(fig, '76-071')
