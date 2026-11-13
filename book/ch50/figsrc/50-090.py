import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 10, 70, 28, 1, 7, 1, arrow_right=True)
box(ax, f(1) - 5, 36, f(2) - f(1) + 10, 14, 'varie', fill=False, dash=True)
text(ax, (f(1) + f(2)) / 2, 54, r'divise $q = 2$ : 1 ou 2', 'varie', 's')
disc(ax, f(1), 43, 3, 'resultat', label='1', size='s'); disc(ax, f(2), 43, 3, 'limite', label='2', size='s')
arrow(ax, (f(1), 39.6), (f(1), 30.4), 'resultat'); arrow(ax, (f(2), 39.6), (f(2), 30.4), 'limite')
for v in (1, 4, 7): disc(ax, f(v), 28, 2.0, 'resultat', fill=False, lw=1.2)
disc(ax, f(2), 28, 2.0, 'limite', fill=False, lw=1.2)
for a, b in ((1, 4), (4, 7)):
    arrow(ax, (f(a), 21), (f(b), 21), 'varie', lw=1.0, curve=0.35)
    text(ax, (f(a) + f(b)) / 2, 12.5, r'$+3$', 'varie', 's')
text(ax, 44, 4, r'$\equiv 1\ (\mathrm{mod}\ 3)$ : 1, 4, 7', 'resultat', 's')
save(fig, '50-090')
