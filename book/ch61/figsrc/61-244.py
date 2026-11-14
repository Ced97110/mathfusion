import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 12, 76, 22, -2, 2, 1, arrow_right=False)
r2 = 2 ** 0.5
for v, l in [(-r2, r'$-\sqrt{2}$'), (r2, r'$\sqrt{2}$')]:
    disc(ax, f(v), 22, 2, 'resultat'); text(ax, f(v), 14, l, 'resultat', 's')
box(ax, 30, 46, 28, 10, 'sujet', label=r'$u=\sqrt{2}$')
arrow(ax, (38, 46), (f(-r2), 25), 'varie'); arrow(ax, (50, 46), (f(r2), 25), 'varie')
line(ax, [(44, 46), (44, 26)], 'limite', dash=True); text(ax, 44, 29, '×', 'limite', 'l')
text(ax, 44, 59, r'racines de $x^2-2$', 'resultat', 's')
text(ax, 44, 5, 'les seules images possibles', 'varie', 's')
save(fig, '61-244')
