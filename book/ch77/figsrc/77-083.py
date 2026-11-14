import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def brackets(ax, cx, cy, w, h):
    for s in (-1, 1):
        x = cx + s * w / 2
        line(ax, [(x - s * 1.2, cy + h / 2), (x, cy + h / 2), (x, cy - h / 2), (x - s * 1.2, cy - h / 2)], "encre", lw=0.8)
def cells(ax, cx, cy, vals, roles, dx=9, dy=7, size="m"):
    out = []
    for i in range(2):
        for j in range(2):
            x = cx + (j - 0.5) * dx; y = cy + (0.5 - i) * dy
            text(ax, x, y, vals[2 * i + j], roles[2 * i + j], size)
    brackets(ax, cx, cy, dx + 6, dy + 4)

fig, ax = canvas(62)
cx, cy = 20, 42
cells(ax, cx, cy, ['0', '2', '1', '0'], ['resultat', 'varie', 'varie', 'resultat'])
text(ax, cx, cy + 9.5, r'$\rho(\sqrt{2})$', 'sujet', 'm')
text(ax, 58, cy + 3.5, r'$T=0+0=0$', 'resultat', 'm')
text(ax, 58, cy - 3.5, r'$N=0\times0-2\times1=-2$', 'varie', 's')
arrow(ax, (cx, 30), (cx, 25), 'encre')
box(ax, 4, 14, 44, 9, 'resultat', label=r'$\lambda^2-0\lambda+(-2)=\lambda^2-2$', size='m')
text(ax, 26, 10, 'polynôme minimal de ' + r'$\sqrt{2}$', 'resultat', 's')
box(ax, 54, 14, 31, 9, 'limite', label=r'$\lambda-c$ : impossible', size='s')
text(ax, 69.5, 10, r'$\sqrt{2}\neq c$ (fraction)', 'limite', 's')
text(ax, 44, 3.5, r'$\sqrt{2}$ est racine : $(\sqrt{2})^2-2=0$', 'encre', 's')
save(fig, '77-083')
