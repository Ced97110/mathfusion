import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'$\mathbb{Z}/2\oplus\mathbb{Z}/2$ : 4 éléments', 'sujet', 'm')
els = [('(0, 0)', 'ordre 1', 'fixe'), ('(0, 1)', 'ordre 2', 'sujet'), ('(1, 0)', 'ordre 2', 'sujet'), ('(1, 1)', 'ordre 2', 'sujet')]
for k, (e, o, r) in enumerate(els):
    x = 2 + k * 21.5
    box(ax, x, 38, 19, 12, r, label=e)
    text(ax, x + 9.5, 33, o, r, 's')
text(ax, 44, 22, 'p = 2 premier : ordre 2 existe', 'resultat', 's')
text(ax, 44, 12, '4 non premier : aucun ordre 4', 'limite', 's')
save(fig, '60-114')
