import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 70, 22, -14, 2, 2, arrow_right=False, every=2)
for v, lab, dy in ((-13, r'$(2,3)$', 8), (-1, r'$(1,0)$', 8), (0, r'$(0,0)$', 15)):
    disc(ax, f(v), 22, 1.1, 'sujet'); line(ax, [(f(v), 23.2), (f(v), 22 + dy - 2)], 'sujet', lw=0.6); text(ax, f(v), 22 + dy, lab, 'sujet', 's')
disc(ax, f(1), 22, 1.1, 'limite'); text(ax, f(1) + 1, 31, r'$1$ jamais atteint', 'limite', 's', ha='left'); line(ax, [(f(1), 23.2), (f(1), 29.5)], 'limite', lw=0.6, dash=True)
text(ax, 44, 46, r'$-x^2-y^2=-13,\ -1,\ 0$ : jamais $1$', 'encre', 's')
text(ax, 44, 6, r'valeurs de $-x^2-y^2$ : toujours $\leq 0$', 'limite', 's')
text(ax, 22, 38, 'rang 2 : non dégénérée', 'fixe', 's')
save(fig, '71-195')
