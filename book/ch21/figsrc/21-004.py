import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$\frac{120}{v}$ pour quelques $v$', 'sujet', 'l')
for i, (v, r) in enumerate([(60, 2), (40, 3), (30, 4), (0, None)]):
    x = 4 + i * 21
    box(ax, x, 33, 17, 9, 'varie', label=rf'$v = {v}$', size='s')
    if r is not None:
        arrow(ax, (x + 8.5, 32.5), (x + 8.5, 24), 'resultat'); box(ax, x, 12, 17, 11, 'resultat', label=str(r))
    else:
        arrow(ax, (x + 8.5, 32.5), (x + 8.5, 24), 'limite'); box(ax, x, 12, 17, 11, 'limite', fill=False, dash=True, label='rien', size='s')
text(ax, 71.5, 5, 'trou : aucun résultat', 'limite', 's')
save(fig, '21-004')
