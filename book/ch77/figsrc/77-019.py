import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(48)
mat(ax, 20, 20, [r'$2\quad-1$', r'$1\quad\hspace{0.7}2$'], 'sujet')
text(ax, 36, 20, r'$\times$', 'encre', 'l')
mat(ax, 48, 20, ['$3$', '$4$'], 'fixe', hw=3.5)
arrow(ax, (55, 20), (63, 20), 'resultat')
mat(ax, 73, 20, ['$2$', '$11$'], 'resultat', hw=4.5)
text(ax, 20, 36, r'$\rho(2+i)$', 'sujet', 's'); text(ax, 48, 36, r'$3+4i$', 'fixe', 's'); text(ax, 73, 36, r'$2+11i$', 'resultat', 's')
text(ax, 44, 5, r'comme $(2+i)(3+4i)=2+11i$', 'encre', 's')
save(fig, '77-019')
