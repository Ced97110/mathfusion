import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, u = 16, 8, 7
g = lambda a, b: (ox + a*u, oy + b*u)
for i in range(-1, 4):
    for j in range(7): disc(ax, *g(i, j), 0.7, 'fixe')
arrow(ax, g(0, 0), g(3, 2), 'sujet', lw=1.3); arrow(ax, g(3, 2), g(2, 6), 'varie', lw=1.3); arrow(ax, g(0, 0), g(2, 6), 'resultat', lw=1.3)
text(ax, g(3, 2)[0] + 8, g(3, 2)[1] - 1, '(3 ; 2)', 'sujet', 's')
text(ax, g(2.5, 4)[0] + 11, g(2.5, 4)[1], '(−1 ; 4)', 'varie', 's')
text(ax, g(2, 6)[0], g(2, 6)[1] + 4.5, '(2 ; 6)', 'resultat', 's')
box(ax, 52, 36, 34, 9, 'sujet', label=r'translation $mx+ny$')
box(ax, 52, 18, 34, 9, 'autre', label=r'couple $(m\,;\,n)$')
arrow(ax, (69, 36), (69, 28), 'varie', both=True)
text(ax, 69, 11, 'enchaîner = additionner', 'resultat', 's')
text(ax, 69, 54, r'$T \simeq$ ℤ × ℤ', 'encre', 'l')
save(fig, '74-075')
