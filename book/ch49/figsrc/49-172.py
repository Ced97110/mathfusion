import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(95)
box(ax, 4, 62, 26, 26, 'sujet'); box(ax, 58, 62, 26, 26, 'resultat')
text(ax, 17, 92, r'Stab $A$', 'sujet', 's'); text(ax, 71, 92, r'Stab $B$', 'resultat', 's')
for y, l, m in ((80, r'$e$', r'$e$'), (68, r'$s$', r"$s'$")):
    disc(ax, 17, y, 4, 'sujet', label=l, size='s'); disc(ax, 71, y, 4, 'resultat', label=m, size='s')
    arrow(ax, (21.5, y), (66.5, y), 'varie')
text(ax, 44, 48, r"$s' = r\,s\,r^{-1}$", 'varie', 'm')
xs = [10, 32, 56, 78]
for x, n, r in zip(xs, 'BAAB', ('resultat', 'sujet', 'sujet', 'resultat')): disc(ax, x, 26, 4, r, label=n, size='m')
for i, l in enumerate((r'$r^{-1}$', r'$s$', r'$r$')):
    arrow(ax, (xs[i] + 4.5, 26), (xs[i+1] - 4.5, 26), 'varie'); text(ax, (xs[i] + xs[i+1]) / 2, 33, l, 'varie', 's')
save(fig, '49-172')
