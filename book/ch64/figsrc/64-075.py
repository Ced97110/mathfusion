import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
labs = [r'$S_4$ (24)', r'$A_4$ (12)', r'$V$ (4)', r'$W$ (2)', r'$\{e\}$ (1)']
facs = [r'$\mathbb{Z}/2$', r'$\mathbb{Z}/3$', r'$\mathbb{Z}/2$', r'$\mathbb{Z}/2$']
ys = [60 - 13 * i for i in range(5)]
for i, y in enumerate(ys):
    box(ax, 4, y, 30, 7, 'varie' if i == 3 else 'sujet', label=labs[i])
    if i < 4:
        arrow(ax, (19, y), (19, ys[i + 1] + 7), 'fixe')
        text(ax, 23, y - 3, facs[i], 'resultat', 's', ha='left')
text(ax, 40, ys[3] + 3.5, r'$W=\{e,(12)(34)\}$', 'varie', 's', ha='left')
save(fig, '64-075')
