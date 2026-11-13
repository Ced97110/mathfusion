import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [r"$v'$", r"$v'\cdot 1$", r"$v'(uv)$", r"$(v'u)v$", r"$1\cdot v$", r"$v$"]
notes = [r'on multiplie par $1$', r'on remplace $1$ par $uv$', 'on regroupe', r"$v'u = 1$", r'$1\cdot v = v$']
roles = ['sujet', 'fixe', 'fixe', 'fixe', 'fixe', 'resultat']
ys = [72 - 13 * i for i in range(6)]
for i, (r, y, ro) in enumerate(zip(rows, ys, roles)):
    box(ax, 8, y - 4.5, 26, 9, 'varie' if i == 3 else ro, label=r)
    if i < 5:
        arrow(ax, (21, y - 4.5), (21, ys[i + 1] + 4.5), 'varie' if i == 2 else 'fixe')
        text(ax, 40, (y + ys[i + 1]) / 2, notes[i], 'varie' if i == 2 else 'encre', 's', ha='left', weight='bold' if i == 2 else 'normal')
text(ax, 62, 7, '', 'encre', 's')
save(fig, '44-097')
