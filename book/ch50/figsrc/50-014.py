import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for x, w, t, role in [(2, 20, 'origine', 'fixe'), (28, 36, 'trois énoncés', 'sujet'), (69, 18, 'usages', 'resultat')]:
    box(ax, x, 6, w, 38, role); text(ax, x + w / 2, 49, t, role, 's')
text(ax, 12, 28, 'actions de\ngroupes', 'fixe', 's'); text(ax, 12, 19, 'chapitre 49', 'fixe', 's')
stm = ['I : existence de $p^k$', 'II : $p$-Sylow conjugués', r'III : $n_p \equiv 1$ (mod $p$)']
for i, s in enumerate(stm):
    box(ax, 30, 31 - 11 * i, 32, 9, 'sujet', label=s, size='s', r=0.5)
for i, n in enumerate([12, 15, 30]):
    box(ax, 71, 31 - 11 * i, 14, 9, 'resultat', label=f'ordre {n}', size='s', r=0.5)
arrow(ax, (22.5, 25), (27.5, 25), 'varie'); arrow(ax, (64.5, 25), (69.5, 25), 'varie')
save(fig, '50-014')
