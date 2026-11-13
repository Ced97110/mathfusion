import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, 'une classe de matrices', 'encre', 'm')
box(ax, 2, 4, 84, 52, 'sujet', fill=False, dash=True)
def mat(cx, cy, vals, role, hw):
    for (i, j), v in zip([(0,0),(0,1),(1,0),(1,1)], vals):
        text(ax, cx + (j - 0.5) * 2 * hw * 0.5 * 1.0, cy + (0.5 - i) * 10, v, role, 'm')
    for sgn in (-1, 1):
        x = cx + sgn * (hw + 3)
        line(ax, [(x - sgn * 1.5, cy + 9), (x, cy + 9), (x, cy - 9), (x - sgn * 1.5, cy - 9)], role, lw=0.9)
mat(22, 32, [r'$-18$', r'$33$', r'$-11$', r'$20$'], 'fixe', 10)
mat(66, 32, [r'$1$', r'$2$', r'$-1$', r'$1$'], 'resultat', 8)
arrow(ax, (38, 32), (48, 32), 'varie')
text(ax, 22, 12, 'plus compliquée', 'fixe', 's')
text(ax, 66, 12, 'la plus simple', 'resultat', 's')
save(fig, '43-149')
