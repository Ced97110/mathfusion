import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(54)
x0, L = 8.0, 70.0; x1 = x0 + L; xt = x0 + L / 3
for y in (38, 14):
    box(ax, x0, y, L, 7, 'fixe', r=0.3)
    box(ax, x0, y, L / 3, 7, 'sujet', r=0.3)
text(ax, x0, 48, '0', 'fixe', 's'); text(ax, xt, 48, r'$d$ = 60', 'sujet', 's'); text(ax, x1, 48, '180', 'fixe', 's')
text(ax, x0, 9, '0', 'fixe', 's'); text(ax, xt, 9, r'$\theta$', 'sujet', 's'); text(ax, x1, 9, r'$\pi$', 'fixe', 's')
line(ax, [(xt, 38), (xt, 21)], 'sujet', dash=True)
line(ax, [(x1, 38), (x1, 21)], 'fixe', dash=True)
text(ax, x0 + L / 6 - 2, 29.5, 'un tiers', 'sujet', 's')
text(ax, 55, 29.5, r'$d$/180 = $\theta$/$\pi$ : même part', 'resultat', 's')
save(fig, '29-053')
