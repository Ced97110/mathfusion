import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
y0 = 22.0
f = lambda k: 12 + (k + 2) * 12.4
line(ax, [(5, y0), (83, y0)], 'fixe')
for k in range(-2, 4):
    used = k in (-2, 1, 3)
    disc(ax, f(k), y0, 1.5 if used else 1.0, 'sujet' if used else 'fixe')
text(ax, f(-2), y0 - 5, r'$-2u=(-4\,;\,-2)$', 'sujet', 's')
text(ax, f(1), y0 - 5, r'$u=(2\,;\,1)$', 'resultat', 's')
text(ax, f(3), y0 - 5, r'$3u=(6\,;\,3)$', 'sujet', 's')
disc(ax, f(1), y0, 1.5, 'resultat')
arrow(ax, (f(3) - 1, y0 + 2), (f(1) + 1, y0 + 2), 'varie', curve=0.45)
arrow(ax, (f(-2) + 1, y0 + 2), (f(1) - 1, y0 + 2), 'varie', curve=-0.45)
text(ax, 44, 48, r'$3u+(-2)u=(3-2)u=u$', 'resultat', 'm')
text(ax, 44, 8, r'les points $ku$, $k$ entier', 'fixe', 's')
save(fig, '57-127')
