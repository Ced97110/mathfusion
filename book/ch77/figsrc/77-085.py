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

fig, ax = canvas(46)
y = 26
A = ['0', '2', '1', '0']
cells(ax, 14, y, A, ['varie', 'varie', 'varie', 'varie'])
text(ax, 27, y, r'$\times$', 'encre', 'm')
cells(ax, 40, y, A, ['varie'] * 4)
text(ax, 53, y, r'$=$', 'encre', 'm')
cells(ax, 66, y, ['2', '0', '0', '2'], ['resultat'] * 4)
box(ax, 7.5, y + 0.4, 13, 5.2, 'sujet', fill=False, lw=1.0, dash=True)
box(ax, 33.2, y - 6.2, 6.6, 12.4, 'autre', fill=False, lw=1.0, dash=True)
text(ax, 66, y - 12, r'$=2\cdot1$', 'resultat', 'm')
text(ax, 14, y + 12, r'$\rho(\sqrt{2})$', 'varie', 's')
text(ax, 40, y + 12, r'$\rho(\sqrt{2})$', 'varie', 's')
text(ax, 30, 6, r'1re ligne $\times$ 1re colonne : $0\times0+2\times1=2$', 'encre', 's')
save(fig, '77-085')
