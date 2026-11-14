import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [14, 34, 54, 74]
top = [('0', 'resultat'), ('1', 'resultat'), (r'$\alpha$', 'varie'), (r'$\alpha+1$', 'varie')]
bot = [('0', 'resultat'), ('1', 'resultat'), (r'$\alpha+1$', 'varie'), (r'$\alpha$', 'varie')]
yt, yb = 48, 14
for x, (s, r) in zip(xs, top): box(ax, x - 8, yt - 4, 16, 8, r, label=s)
for x, (s, r) in zip(xs, bot): box(ax, x - 8, yb - 4, 16, 8, r, label=s)
arrow(ax, (xs[0], yt - 5), (xs[0], yb + 5), 'resultat')
arrow(ax, (xs[1], yt - 5), (xs[1], yb + 5), 'resultat')
arrow(ax, (xs[2], yt - 5), (xs[3], yb + 5), 'varie')
arrow(ax, (xs[3], yt - 5), (xs[2], yb + 5), 'varie')
text(ax, 44, 58, r'on élève au carré : $u\mapsto u^2$', 'encre', 's')
brace(ax, xs[0] - 8, xs[1] + 8, 8, 'resultat', label=r'fixés : $\mathbb{F}_2$', down=True, depth=1.6)
brace(ax, xs[2] - 8, xs[3] + 8, 8, 'varie', label='déplacés', down=True, depth=1.6)
save(fig, '67-091')
