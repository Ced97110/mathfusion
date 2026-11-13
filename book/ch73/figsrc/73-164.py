import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
labs = [(r'$D$', 'sujet'), (r'$T(1)$', 'varie'), (r'$D^{-1}$', 'sujet'), (r'$T(-1)$', 'varie')]
x0, bw, gap, y = 5.5, 17, 3, 46
for i, (l, r) in enumerate(labs):
    box(ax, x0 + i * (bw + gap), y, bw, 9, r, label=l)
brace(ax, x0, x0 + 3 * bw + 2 * gap, y + 9, 'fixe', label='trois facteurs : pente 9', down=False)
text(ax, x0 + 3 * (bw + gap) + bw / 2, y - 4, 'retire 1', 'varie', 's')
box(ax, 20, 12, 48, 10, 'resultat', label='pente 8 = 1 × (9 − 1)')
arrow(ax, (x0 + 1.5 * bw + gap, y - 1), (36, 23), 'fixe')
arrow(ax, (x0 + 3 * (bw + gap) + bw / 2, y - 7), (60, 23), 'varie')
save(fig, '73-164')
