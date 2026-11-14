import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
f = numberline(ax, 6, 78, 24, 0, 10, labels=False, arrow_right=False)
line(ax, [(f(1) + 1.3, 24), (f(10) - 1.3, 24)], 'sujet', lw=3)
disc(ax, f(1), 24, 1.3, 'sujet'); disc(ax, f(10), 24, 1.3, 'sujet', fill=False)
for v, s in [(2.9, '2,9'), (4.21, '4,21')]:
    disc(ax, f(v), 24, 1.1, 'resultat'); text(ax, f(v), 30, s, 'resultat', 's')
text(ax, f(0), 17, '0', 'fixe', 's')
text(ax, f(1) + 1, 17, '1 inclus', 'sujet', 's')
text(ax, f(10) - 2, 17, '10 exclu', 'sujet', 's')
text(ax, 44, 46, r'$1\leq m<10$', 'sujet', 'l')
save(fig, '14-071')
