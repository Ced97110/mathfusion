import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def tiles(x, y, s, role):
    for i, l in enumerate(s): box(ax, x + i * 9, y, 8.5, 9, role, label=f'${l}$')
tiles(6, 44, 'xy', 'sujet'); tiles(62, 44, 'yx', 'autre')
text(ax, 15, 56, '2 lettres', 'sujet', 's'); text(ax, 71, 56, '2 lettres', 'autre', 's')
src = [(6, 'sujet'), (15, 'sujet'), (62, 'autre'), (71, 'autre')]
dst = 26 + 0
for i, (sx, role) in enumerate(src):
    dx = 26 + i * 9
    line(ax, [(sx + 4.25, 44), (dx + 4.25, 21)], role, lw=0.7)
tiles(26, 12, 'xy', 'sujet'); tiles(44, 12, 'yx', 'autre')
brace(ax, 26, 61.5, 12, 'resultat', label='4 lettres = 2 + 2')
save(fig, '49-027')
