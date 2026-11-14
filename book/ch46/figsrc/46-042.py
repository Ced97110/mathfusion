import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, a, role, cw=6.5, rh=5.5):
    for i in range(2):
        for j in range(2):
            text(ax, cx + (j - 0.5) * cw, cy + (0.5 - i) * rh, a[i][j], role, 'm')
    for s in (-1, 1):
        x = cx + s * (cw + 1.2)
        line(ax, [(x - s * 1.2, cy + rh + 0.2), (x, cy + rh + 0.2), (x, cy - rh - 0.2), (x - s * 1.2, cy - rh - 0.2)], role, lw=0.9)

fig, ax = canvas(70)
box(ax, 3, 3, 42, 64, 'fixe', dash=True)
text(ax, 24, 62, r'$GL_2(\mathbb{R})$', 'fixe', 'm')
mat(ax, 24, 38, [['1', '1'], ['0', '1']], 'resultat')
text(ax, 24, 22, 'déterminant 1', 'resultat', 's'); text(ax, 24, 14, 'inversible', 'resultat', 's')
mat(ax, 66, 38, [['1', '2'], ['2', '4']], 'limite')
text(ax, 66, 22, 'déterminant 0', 'limite', 's'); text(ax, 66, 14, 'pas inversible', 'limite', 's')
text(ax, 66, 54, 'hors du groupe', 'limite', 's')
save(fig, '46-042')
