import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 70, 24, 0, 7)
for v, r, t in [(2, 'sujet', r'$x_1=2$'), (6, 'autre', r'$x_2=6$')]:
    disc(ax, f(v), 24, 2.0, r)
    line(ax, [(f(v), 27), (f(v), 42)], 'fixe', dash=True)
    text(ax, f(v), 31, t, r, 'm')
arrow(ax, (f(2), 42), (f(6), 42), 'varie')
text(ax, (f(2) + f(6)) / 2, 47, 'avancée', 'varie', 'm')
text(ax, (f(2) + f(6)) / 2, 54, r'$x_2-x_1=6-2=4$', 'resultat', 'l', weight='bold')
save(fig, '19-071')
