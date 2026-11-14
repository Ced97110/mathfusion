import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
xs0 = [8, 52]
def diag(x0, yt, s, role, name):
    xs = [x0 + 9 * i for i in range(4)]
    for i, x in enumerate(xs):
        disc(ax, x, yt, 1.3, 'fixe'); disc(ax, x, yt - 14, 1.3, 'fixe')
    for i, x in enumerate(xs):
        arrow(ax, (x, yt - 1.5), (xs[(i + s) % 4], yt - 12.5), role, lw=0.8)
    text(ax, x0 + 13.5, yt - 22, name, role, 's')
    return xs
xa = diag(8, 86, 0, 'fixe', 'ligne de 0 (identité)')
diag(52, 86, 1, 'varie', 'ligne de 1')
diag(8, 50, 2, 'sujet', 'ligne de 2')
diag(52, 50, 3, 'autre', 'ligne de 3')
for i, x in enumerate(xa):
    text(ax, x, 92, str(i), 'encre', 's'); text(ax, x, 68, str(i), 'encre', 's')
text(ax, 44, 22, 'chaque ligne : chaque heure une fois', 'resultat', 's')
text(ax, 44, 14, r'4 permutations sur les 24 de $S_4$', 'sujet', 's')
text(ax, 44, 6, r'elles se combinent comme $\mathbb{Z}/4$', 'fixe', 's')
save(fig, '45-220')
