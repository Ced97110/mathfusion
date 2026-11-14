import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 63, 'diviseurs de 329', 'encre', 's')
xs = [3.5, 24.5, 45.5, 66.5]
for x, d, r, role in zip(xs, ['1', '7', '47', '329'], ['reste 1', 'reste 2', 'reste 2', 'reste 4'], ['resultat', 'limite', 'limite', 'limite']):
    box(ax, x, 50, 18, 9, 'sujet', label=d, size='m')
    arrow(ax, (x + 9, 49.5), (x + 9, 45.5), 'fixe')
    box(ax, x, 36, 18, 9, role, label=r, size='s')
text(ax, 44, 31, 'restes dans la division par 5', 'encre', 's')
arrow(ax, (12.5, 35.5), (12.5, 24), 'resultat')
box(ax, 3.5, 6, 81, 18, 'resultat', label=r"$n_5=1$ : $H_2$ est normal" + "\n" + r"et $G'\subseteq H_2$", size='m')
save(fig, '50-219')
