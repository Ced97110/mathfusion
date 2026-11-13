import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 12, 44, r'$3\times5$', 'encre', 'l')
arrow(ax, (22, 44), (33, 44), 'fixe')
box(ax, 35, 38, 14, 12, 'limite', label='15')
text(ax, 70, 44, 'pas somme de 3 carrés', 'limite', 's')
text(ax, 44, 22, 'nombre de carrés', 'fixe', 's')
f = lambda n: 8 + (n - 1) * 8.2
for n in range(1, 11):
    ok = n in (1, 2, 4, 8)
    disc(ax, f(n), 11, 3.6, 'resultat' if ok else 'limite', label=str(n))
arrow(ax, (38, 37), (f(3) + 1, 15.5), 'limite', lw=0.9, curve=0.0)
save(fig, '78-011')
