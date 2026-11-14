import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [('libre', 'sujet', [1, 1, 1, 1]), ('triviale', 'autre', [4, 4, 4, 4]), ('ordinaire', 'fixe', [4, 2, 1, 1])]
cw = 27.0
for i, (name, role, st) in enumerate(cols):
    cx = 4 + cw * i + cw / 2
    box(ax, 4 + cw * i + 0.5, 4, cw - 1, 54, role, fill=False, lw=1.2 if i == 0 else 0.8)
    text(ax, cx, 52, name, role, 'l', weight='bold')
    for k, s in enumerate(st):
        y = 42 - k * 9.5
        disc(ax, cx - 6, y, 3.2, role, label=None)
        text(ax, cx + 5, y, str(s), role, 'l')
text(ax, 4 + cw * 0 + cw / 2, 8, 'seul le neutre', 'sujet', 's')
text(ax, 4 + cw * 1 + cw / 2, 8, 'tous fixent tout', 'autre', 's')
text(ax, 4 + cw * 2 + cw / 2, 8, 'tailles mélangées', 'fixe', 's')
text(ax, 44, 59.5, 'taille du stabilisateur de chaque point', 'encre', 's')
save(fig, '49-288')
