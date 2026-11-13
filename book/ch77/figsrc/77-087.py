import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def brackets(ax, cx, cy, w, h):
    for s in (-1, 1):
        x = cx + s * w / 2
        line(ax, [(x - s * 1.2, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.2, cy - h / 2)], "encre", lw=0.8)
def cells(ax, cx, cy, vals, roles, dx=7, dy=6, size="m"):
    for i in range(2):
        for j in range(2):
            text(ax, cx + (j - 0.5) * dx, cy + (0.5 - i) * dy, vals[2 * i + j], roles[2 * i + j], size)
    brackets(ax, cx, cy, dx + 5, dy + 3.5)

fig, ax = canvas(52)
y = 30
cells(ax, 13, y, ['3', '4', '2', '3'], ['sujet'] * 4, dx=7)
text(ax, 25, y, r'$\times$', 'encre', 'm')
cells(ax, 38, y, ['3', '−4', '−2', '3'], ['resultat', 'resultat', 'resultat', 'resultat'], dx=8)
text(ax, 52, y, r'$=$', 'encre', 'm')
cells(ax, 63, y, ['1', '0', '0', '1'], ['fixe'] * 4, dx=7)
box(ax, 32.3, y - 7.2, 5.4, 14.4, 'autre', fill=False, lw=1.0, dash=True)
text(ax, 13, y + 11, 'matrice', 'sujet', 's'); text(ax, 38, y + 11, 'inverse', 'resultat', 's'); text(ax, 63, y + 11, 'identité', 'fixe', 's')
text(ax, 38, y - 13, r'1re colonne : $3-2\sqrt{2}$', 'autre', 's')
text(ax, 44, 8, r'$N=9-8=1$ : $\det=1$, entiers', 'sujet', 's')
save(fig, '77-087')
