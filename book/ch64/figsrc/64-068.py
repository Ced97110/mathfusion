import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 19, 61, 'suite normale quelconque', 'sujet', 's')
text(ax, 69, 61, 'suite dérivée', 'autre', 's')
ys = [44, 28, 12]
L = [r'$G_1$', r'$G_2$', r'$G_3$']
R = [r'$G$', r'$G^{\prime}$', r'$G^{\prime\prime}$']
M = ['=', r'$\supseteq$', r'$\supseteq$']
wl = [34, 30, 26]   # le terme bleu est au moins aussi grand que le terme violet
wr = [34, 22, 14]
for i, y in enumerate(ys):
    box(ax, 19 - wl[i] / 2, y, wl[i], 9, 'sujet', label=L[i])
    box(ax, 69 - wr[i] / 2, y, wr[i], 9, 'autre', label=R[i])
    text(ax, 44, y + 4.5, M[i], 'fixe' if i == 0 else 'varie', 'l', weight='bold')
    if i < 2:
        arrow(ax, (19, y), (19, ys[i + 1] + 9), 'fixe')
        arrow(ax, (69, y), (69, ys[i + 1] + 9), 'fixe')
text(ax, 44, 3, r'$G_{i+1}\supset G^{(i)}$ à chaque étage', 'varie', 's')
save(fig, '64-068')
