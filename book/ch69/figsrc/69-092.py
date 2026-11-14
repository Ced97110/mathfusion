import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
f = numberline(ax, 8, 70, 14, -2, 2, 1)
V = {-2: 3, 0: 2, 1: 1, 2: 0}
for v, n in V.items():
    line(ax, [(f(v), 15.5), (f(v), 22.3)], 'fixe', dash=True, lw=0.6)
    disc(ax, f(v), 26.5, 4.2, 'sujet', label=rf'$V={n}$', size='s')
for a, b in ((-2, 0), (0, 1), (1, 2)):
    box(ax, f(a) + 1, 33, f(b) - f(a) - 2, 9, 'resultat', label=rf'${V[a]}-{V[b]}={V[a] - V[b]}$', size='s')
text(ax, 44, 3.5, 'une racine par morceau', 'resultat', 's')
save(fig, '69-092')
