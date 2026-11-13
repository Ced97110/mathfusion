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
y = 24
text(ax, 44, 41, r'$3+2\sqrt{2}=3\cdot1+2\cdot\sqrt{2}$', 'encre', 'm')
text(ax, 5, y, r'$3\times$', 'sujet', 'm')
cells(ax, 20, y, ['1', '0', '0', '1'], ['sujet'] * 4)
text(ax, 34.5, y, r'$+\,2\times$', 'varie', 'm')
cells(ax, 51, y, ['0', '2', '1', '0'], ['varie'] * 4)
text(ax, 64.5, y, r'$=$', 'encre', 'm')
cells(ax, 77, y, ['3', '4', '2', '3'], ['resultat'] * 4)
text(ax, 20, 13, r'$3\cdot1$', 'sujet', 's')
text(ax, 51, 13, r'$2\,\rho(\sqrt{2})$', 'varie', 's')
text(ax, 77, 13, r'$\rho(3+2\sqrt{2})$', 'resultat', 's')
text(ax, 44, 5, r'$a=3$ devant 1, $b=2$ devant $\sqrt{2}$', 'encre', 's')
save(fig, '77-084')
