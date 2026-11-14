import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y0 = 24.0
xs = [12, 34, 56, 78]
line(ax, [(5, y0), (xs[-1] + 5, y0)], 'fixe')
roles = ['fixe', 'sujet', 'sujet', 'resultat']
for x, r in zip(xs, roles):
    disc(ax, x, y0, 1.6, r)
names = ['$0$', r'$u=(2\,;\,1)$', r'$2u=(4\,;\,2)$', r'$3u=(6\,;\,3)$']
for x, s, r in zip(xs, names, roles):
    text(ax, x, y0 - 6, s, r, 's')
for i in range(3):
    arrow(ax, (xs[i] + 2, y0 + 1.5), (xs[i + 1] - 2, y0 + 1.5), 'varie', curve=-0.5)
    text(ax, (xs[i] + xs[i + 1]) / 2, y0 + 8, r'$+\,u$', 'varie', 's')
text(ax, 44, 44, r'$3\cdot u=u+u+u$', 'resultat', 'l')
text(ax, 44, 7, 'l’action de 3 n’est que l’addition', 'encre', 's')
save(fig, '57-130')
