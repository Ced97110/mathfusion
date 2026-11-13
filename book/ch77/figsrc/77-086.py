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

fig, ax = canvas(50)
cells(ax, 18, 33, [r'$a$', r'$2b$', r'$b$', r'$a$'], ['sujet', 'varie', 'varie', 'sujet'], dx=9, dy=7)
text(ax, 18, 44, r'$\rho(a+b\sqrt{2})$', 'encre', 's')
text(ax, 58, 38, r'$T=a+a=2a$', 'sujet', 'm')
text(ax, 58, 28, r'$N=a\cdot a-2b\cdot b$', 'varie', 's')
text(ax, 58, 23.5, r'$=a^2-2b^2$', 'varie', 's')
line(ax, [(4, 17), (84, 17)], 'fixe', dash=True)
text(ax, 25, 11, r'$3+2\sqrt{2}$ : $T=6$, $N=1$', 'resultat', 's')
text(ax, 25, 5, r'$1+3\sqrt{2}$ : $T=2$, $N=-17$', 'resultat', 's')
save(fig, '77-086')
