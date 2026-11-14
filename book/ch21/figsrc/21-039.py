import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 6, 62, 76, 12, 'sujet', label=r'$x^2-2x-15=(x+3)(x-5)$', size='s')
box(ax, 8, 40, 30, 11, 'varie', label=r'$x+3=0$'); box(ax, 50, 40, 30, 11, 'varie', label=r'$x-5=0$')
arrow(ax, (30, 62), (23, 52), 'varie'); arrow(ax, (58, 62), (65, 52), 'varie')
box(ax, 8, 24, 30, 10, 'limite', label=r'$x=-3$'); box(ax, 50, 24, 30, 10, 'limite', label=r'$x=5$')
arrow(ax, (23, 40), (23, 35), 'limite'); arrow(ax, (65, 40), (65, 35), 'limite')
f = numberline(ax, 8, 70, 10, -5, 7, 1, labels=False, arrow_right=True)
for a, b in ((-5, -3), (-3, 5), (5, 7)):
    x0 = f(a) + (0 if a == -5 else 1.8); x1 = f(b) - (0 if b == 7 else 1.8)
    ax.plot([x0, x1], [10, 10], color=COL['resultat'], lw=2.4, zorder=3, solid_capstyle='round')
for v in (-3, 5):
    disc(ax, f(v), 10, 1.5, 'limite', fill=False, lw=1.0); text(ax, f(v), 5.5, f'{v}'.replace('-', '−'), 'limite', 's')
text(ax, f(1), 15, 'domaine : tous sauf −3 et 5', 'resultat', 's')
save(fig, '21-039')
