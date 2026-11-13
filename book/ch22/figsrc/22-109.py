import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
labs = [r'$\sqrt{y-3}=4$', r'$y-3=16$', r'$y=19$', r'$\sqrt{19-3}=\sqrt{16}=4$']
acts = ['au carré', 'on ajoute 3', 'on vérifie']
for i, l in enumerate(labs):
    y = 66 - i * 22
    box(ax, 4, y, 40, 10, 'resultat' if i >= 2 else 'sujet', label=l, size='s' if i == 3 else 'm')
    if i < 3:
        arrow(ax, (24, y), (24, y - 12), 'varie'); text(ax, 28, y - 6, acts[i], 'varie', 's', ha='left')
line(ax, [(44, 5), (52, 5), (52, 71)], 'fixe')
arrow(ax, (52, 71), (44.5, 71), 'fixe')
text(ax, 54, 38, 'équation de départ', 'fixe', 's', ha='left')
save(fig, '22-109')
