import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, a, role, cw=6.5, rh=5.5):
    for i in range(2):
        for j in range(2):
            text(ax, cx + (j - 0.5) * cw, cy + (0.5 - i) * rh, a[i][j], role, 'm')
    for s in (-1, 1):
        x = cx + s * (cw + 1.2)
        line(ax, [(x - s * 1.2, cy + rh + 0.2), (x, cy + rh + 0.2), (x, cy - rh - 0.2), (x - s * 1.2, cy - rh - 0.2)], role, lw=0.9)

fig, ax = canvas(78)
box(ax, 3, 3, 82, 72, 'fixe', dash=True)
text(ax, 44, 70, r'$GL_2(\mathbb{R})$ : matrices inversibles', 'fixe', 's')
box(ax, 7, 12, 74, 51, 'sujet')
text(ax, 44, 58, r'$SL_2(\mathbb{R})$ : déterminant 1', 'sujet', 's')
mat(ax, 20, 40, [['1', '1'], ['0', '1']], 'sujet')
mat(ax, 68, 40, [['1', '−1'], ['0', '1']], 'sujet')
arrow(ax, (31, 43), (55, 43), 'varie'); text(ax, 43, 47, 'inverse', 'varie', 's')
text(ax, 20, 28, 'déterminant 1', 'resultat', 's'); text(ax, 68, 28, 'déterminant 1', 'resultat', 's')
text(ax, 44, 18, "l'inverse reste dans $SL_2$", 'resultat', 's')
save(fig, '46-040')
